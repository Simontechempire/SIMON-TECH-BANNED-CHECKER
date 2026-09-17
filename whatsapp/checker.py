from dataclasses import dataclass


@dataclass
class CheckResult:
    phone: str
    country: str
    status: str
    verified: bool = False
    reason: str = ""


async def check_number(phone: str, country: str) -> CheckResult:
    return CheckResult(
        phone=phone,
        country=country,
        status="Unable to verify",
        verified=False,
        reason="Verification service not connected."
    )
