import logging

logger = logging.getLogger(__name__)


def send_verification_email(email: str, token: str) -> None:
    """Integration seam for a transactional email provider."""
    logger.info("Verification email requested for %s", email)
    logger.debug("Verification token generated: %s", token)


def send_password_reset_email(email: str, token: str) -> None:
    """Integration seam for a transactional email provider."""
    logger.info("Password reset email requested for %s", email)
    logger.debug("Password reset token generated: %s", token)
