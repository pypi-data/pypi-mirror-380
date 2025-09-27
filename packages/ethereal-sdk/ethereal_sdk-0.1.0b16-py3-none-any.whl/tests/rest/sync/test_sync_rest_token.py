"""Pure sync tests for token operations."""

import pytest


def test_prepare_withdraw_token(rc_ro, sid):
    sub = next(s for s in rc_ro.list_subaccounts(sender=rc_ro.chain.address) if s.id == sid)
    tokens = rc_ro.list_tokens()
    if not tokens:
        pytest.skip("No tokens available for testing")
    token = tokens[0]
    dto = rc_ro.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=100000, account=rc_ro.chain.address)
    assert isinstance(dto, rc_ro._models.InitiateWithdrawDto)
    assert dto.data.token == token.address and dto.data.subaccount == sub.name and dto.data.amount == 100000 and dto.data.account == rc_ro.chain.address and dto.signature == ""


def test_prepare_and_sign_withdraw_token(rc, sid):
    sub = next(s for s in rc.list_subaccounts(sender=rc.chain.address) if s.id == sid)
    token = rc.list_tokens()[0]
    dto = rc.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=100000, account=rc.chain.address)
    signed = rc.sign_withdraw_token(dto)
    assert isinstance(signed, rc._models.InitiateWithdrawDto) and signed.signature != ""


def test_prepare_with_automatic_signing(rc, sid):
    sub = next(s for s in rc.list_subaccounts(sender=rc.chain.address) if s.id == sid)
    token = rc.list_tokens()[0]
    dto = rc.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=100000, account=rc.chain.address, include_signature=True)
    assert isinstance(dto, rc._models.InitiateWithdrawDto) and dto.signature != ""


def test_prepare_withdraw_token_with_custom_nonce(rc_ro, sid):
    sub = next(s for s in rc_ro.list_subaccounts(sender=rc_ro.chain.address) if s.id == sid)
    tokens = rc_ro.list_tokens()
    if not tokens:
        pytest.skip("No tokens available for testing")
    token = tokens[0]
    nonce = "123456789"
    dto = rc_ro.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=100000, account=rc_ro.chain.address, nonce=nonce)
    assert isinstance(dto, rc_ro._models.InitiateWithdrawDto) and dto.data.nonce == nonce


def test_prepare_withdraw_token_with_custom_signed_at(rc_ro, sid):
    sub = next(s for s in rc_ro.list_subaccounts(sender=rc_ro.chain.address) if s.id == sid)
    token = rc_ro.list_tokens()[0]
    ts = 1620000000
    dto = rc_ro.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=100000, account=rc_ro.chain.address, signed_at=ts)
    assert isinstance(dto, rc_ro._models.InitiateWithdrawDto) and dto.data.signed_at == ts


@pytest.mark.skip(reason="This test actually submits a withdrawal request")
def test_prepare_sign_submit_withdraw_token(rc, sid):
    sub = next(s for s in rc.list_subaccounts(sender=rc.chain.address) if s.id == sid)
    tokens = rc.list_tokens()
    token = next((t for t in tokens if t.name == "USD"))
    dto = rc.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=5, account=rc.chain.address)
    signed = rc.sign_withdraw_token(dto)
    result = rc.withdraw_token(signed, token_id=token.id)
    assert isinstance(result, rc._models.WithdrawDto) and result.token == token.address and result.subaccount == sub.name


@pytest.mark.skip(reason="This test actually submits a withdrawal request")
def test_prepare_sign_submit_withdraw_token_one_step(rc, sid):
    sub = next(s for s in rc.list_subaccounts(sender=rc.chain.address) if s.id == sid)
    tokens = rc.list_tokens()
    token = next((t for t in tokens if t.name == "USD"))
    dto = rc.prepare_withdraw_token(subaccount=sub.name, token=token.address, amount=5, account=rc.chain.address, include_signature=True)
    result = rc.withdraw_token(dto, token_id=token.id)
    assert isinstance(result, rc._models.WithdrawDto) and result.token == token.address and result.subaccount == sub.name