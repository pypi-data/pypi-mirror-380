import logging
import re
from asyncio import run, ensure_future
from decimal import Decimal
from enum import StrEnum
from hashlib import sha256

from playwright.async_api import async_playwright, Page, Locator, Position, Playwright  # , FloatRect
from pyotp import TOTP

# noinspection PyProtectedMember
from playwright._impl._errors import TimeoutError
from pyro_client.client.user import UserClient
from pyrogram.handlers import MessageHandler
from xync_schema.enums import UserStatus
from xync_schema.models import Cur, User, PmAgent, Cred, PmCur, Fiat, TopUp

from xync_client.Abc.PmAgent import PmAgentClient
from xync_client.Gmail import GmClient
from xync_client.Pms.Volet.api import APIClient


class CaptchaException(Exception): ...


class OtpNotSetException(Exception): ...


class NoCodeException(Exception): ...


class NoMailException(Exception): ...


def parse_transaction_info(text: str) -> dict[str, str] | None:
    # Поиск ID транзакции
    transaction_id_match = re.search(r"Transaction ID:\s*([\w-]+)", text)
    # Поиск суммы и валюты
    amount_match = re.search(r"Amount:\s*([+-]?[0-9]*\.?[0-9]+)\s*([A-Z]+)", text)
    # Поиск email отправителя
    sender_email_match = re.search(r"Sender:\s*([\w.-]+@[\w.-]+)", text)

    if transaction_id_match and amount_match and sender_email_match:
        return {
            "transaction_id": transaction_id_match.group(1),
            "amount": amount_match.group(1),
            "currency": amount_match.group(2),
            "sender_email": sender_email_match.group(1),
        }
    return None


class Client(PmAgentClient):
    class Pages(StrEnum):
        base = "https://account.volet.com/"
        LOGIN = base + "login"
        OTP_LOGIN = base + "login/otp"
        # HOME = base + "pages/transaction"
        SEND = base + "pages/transfer/wallet"

    async def check_in(self, amount: int | Decimal | float, cur: str, tid: str | int = None) -> float | None:
        pass

    async def proof(self) -> bytes:
        pass

    uid: int
    agent: PmAgent
    bot: UserClient
    api: APIClient
    page: Page
    gmail: GmClient
    norm: str = "payeer"
    pages: type(StrEnum) = Pages

    def __init__(self, agent: PmAgent):
        super().__init__(agent)
        self.gmail = GmClient(self.uid)
        self.api = APIClient(self.agent.auth["api"], self.agent.auth["password"], self.agent.auth["login"])

    @staticmethod
    def form_redirect(topup: TopUp) -> tuple[str, dict | None]:
        ac_account_email = topup.topupable.auth["ac_account_email"]
        ac_sci_name = topup.topupable.auth["ac_sci_name"]
        ac_order_id = str(topup.id)
        ac_amount = "{0:.2f}".format(topup.amount * 0.01)
        ac_currency = topup.cur.ticker
        ac_comments = "XyncPay top up"
        secret = topup.topupable.auth["secret"]
        data = [ac_account_email, ac_sci_name, ac_amount, ac_currency, secret, ac_order_id]

        ac_sign = sha256(":".join(data).encode()).hexdigest()

        params = {
            "ac_account_email": ac_account_email,
            "ac_sci_name": ac_sci_name,
            "ac_amount": ac_amount,
            "ac_currency": ac_currency,
            "ac_order_id": ac_order_id,
            "ac_sign": ac_sign,
            "ac_comments": ac_comments,
        }
        url = "https://account.volet.com/sci/"
        return url, params

    def get_topup(self, tid: str) -> dict:
        t = self.api.check_by_id(tid)
        return t["status"] == "COMPLETED" and {
            "pmid": t["id"],
            "from_acc": t["walletSrcId"],
            "oid": t["orderId"],
            "amount": int(t["amount"] * 100),
            "ts": t["updatedTime"],
        }

    async def start(self, pw: Playwright, headed: bool = False):
        ensure_future(self.gmail.start(pw, False))
        return await super().start(pw, False, True)

    async def wait_for_code(self, uid: int, topic: str, hg: tuple[MessageHandler, int]) -> str:
        code = await self.bot.wait_from(uid, topic, hg)
        return code and code[-6:]

    async def _login(self):
        ll = self.page.locator("input#j_username")
        await ll.fill("mixartemev@gmail.com")
        await self.page.locator("input#j_password").fill("mixfixX98")
        await self.page.wait_for_timeout(200)
        await ll.click()
        volet_bot_id, topic = 243630567, "otp_login"
        await self.page.locator("input#loginToAdvcashButton", has_text="log in").hover()
        hg = self.bot.subscribe_for(volet_bot_id, topic)  # 243630567 - is volet bot
        await self.page.locator("input#loginToAdvcashButton:not([disabled])", has_text="log in").click()
        await self.page.wait_for_url(self.pages.OTP_LOGIN)
        if not (code := await self.wait_for_code(volet_bot_id, topic, hg)):
            await self.bot.receive("no login code", photo=await self.page.screenshot())
            raise NoCodeException(self.agent.user_id)
        await self.page.locator("input#otpId").fill(code)
        await self.page.click("input#checkOtpButton")
        await self.page.wait_for_url(self.pages.SEND)

    async def send(self, dest: str, amount: float, cur: str) -> tuple[int, bytes, float]:
        curs_map = {"RUB": "Ruble"}

        await self.go(self.pages.SEND)
        await self.page.click("[class=combobox-account]")
        await self.page.click(f'[class=rf-ulst-itm] b:has-text("{curs_map[cur]}") ")')
        await self.page.wait_for_timeout(200)
        await self.page.fill("#srcAmount", str(amount))
        await self.page.fill("#destWalletId", dest)
        await self.page.wait_for_timeout(300)
        await self.page.locator("form#mainForm input[type=submit]", has_text="continue").click()
        # todo: check success confirming
        if otp := self.agent.auth.get("otp"):
            totp = TOTP(otp)
            code = totp.now()
        elif self.agent.user.username.session:
            if not (code := await self.wait_for_code("send")):
                if 1:  # todo: need main confirm
                    await self.gmail.mail_confirm()
                await self.bot.receive("no send trans code", photo=await self.page.screenshot())
                raise NoCodeException(self.agent.user_id)
        else:
            raise OtpNotSetException(self.agent.user_id)
        await self.page.fill("#securityValue", code)
        await self.page.locator("input[type=submit]", has_text="confirm").click()
        await self.page.wait_for_url(self.pages.SEND)
        await self.page.get_by_role("heading").click()
        slip = await self.page.screenshot(clip={"x": 440, "y": 205, "width": 420, "height": 360})
        await self.bot.receive(f"{amount} to {dest} sent", photo=slip)

    async def go(self, url: Pages):
        try:
            await self.page.goto(url)
            if len(await self.page.content()) < 1000:  # todo: fix captcha symptom
                await self.captcha_click()
        except Exception as e:
            await self.bot.receive(repr(e), photo=await self.page.screenshot())
            raise e

    async def send_cap_help(self, xcap: Locator):
        if await xcap.count():
            bb = await xcap.bounding_box(timeout=2000)
            byts = await self.page.screenshot(clip=bb)
            await self.bot.receive("put x, y", photo=byts)
            txt = await self.bot.bot.wait_from(self.bot.me.id, "xy", timeout=59)
            for xy in txt.split(";"):
                px, py = xy
                x, y = bb["x"] + bb["width"] * int(px) / 100, bb["y"] + bb["height"] * int(py) / 100
                await xcap.click(position=Position(x=x, y=y))
            await self.page.wait_for_timeout(1100)
            await self.send_cap_help(xcap)
            # if await (nxt := self.page.locator('button', has_text="Next")).count():
            #     await nxt.click()

    async def captcha_click(self):
        captcha_url = self.page.url
        cbx = self.page.frame_locator("#main-iframe").frame_locator("iframe").first.locator("div#checkbox")
        await cbx.wait_for(state="visible"), await self.page.wait_for_timeout(500)
        await cbx.click(delay=94)
        xcap = self.page.frame_locator("#main-iframe").frame_locator("iframe").last.locator("div.challenge-view")
        if await xcap.count():
            await self.send_cap_help(xcap)
        try:
            await self.page.wait_for_url(lambda url: url != captcha_url)
        except TimeoutError:  # if page no changed -> captcha is undone
            await self.page.screenshot()
            raise CaptchaException(self.page.url)

    async def wait_for_payments(self, interval: int = 29):
        while (await User[self.agent.user_id]).status >= UserStatus.ACTIVE:
            await self.page.reload()
            await self.page.wait_for_timeout(interval * 1000)

    async def upd_balances(self, cur: Cur = None):
        """
        :return: dict {"account number": amount, ...}
        """
        res = self.api.get_balances()
        creds = [
            (
                (
                    await Cred.update_or_create(
                        {"detail": k},
                        pmcur=(await PmCur.get_or_create(pm__norm="volet", cur=await Cur.get(ticker=t)))[0],
                        person_id=self.agent.user.person_id,
                    )
                )[0],
                a,
            )
            for k, (t, a) in res.items()
            if not cur or cur.ticker == t
        ]
        [await Fiat.update_or_create({"amount": amount}, cred=cred) for cred, amount in creds]

    async def stop(self):
        # save state
        self.agent.state = await self.page.context.storage_state()
        await self.agent.save()
        # closing
        await self.bot.stop()
        await self.gmail.stop()
        await self.page.context.close()
        await self.page.context.browser.close()


async def _test():
    from x_model import init_db
    from xync_schema import TORM

    _ = await init_db(TORM, True)
    logging.basicConfig(level=logging.DEBUG)
    uid = 193017646
    playwright: Playwright = await async_playwright().start()
    agent = await PmAgent.get_or_none(pm__norm="volet", user__username_id=uid).prefetch_related(
        "user__username__session"
    )
    if not agent:
        raise Exception(f"No active user #{uid} with agent for volet!")

    va = agent.client()
    try:
        await va.start(playwright)
        await va.send("alena.artemeva25@gmail.com", 7.98)
        await va.wait_for_payments()
    except TimeoutError as te:
        await va.bot.receive(repr(te), photo=await va.page.screenshot())
        raise te
    finally:
        await va.stop()


if __name__ == "__main__":
    run(_test())
