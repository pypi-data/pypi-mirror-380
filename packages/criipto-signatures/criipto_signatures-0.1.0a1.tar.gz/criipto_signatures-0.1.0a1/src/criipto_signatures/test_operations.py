import os
from datetime import datetime
from .__init__ import (
  CriiptoSignaturesSDKAsync,
  CriiptoSignaturesSDKSync,
)
from .operations import (
  QuerySignatureOrders_Viewer_Application,
  CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_PdfDocument,
)
from .models import (
  AddSignatoryInput,
  CancelSignatureOrderInput,
  ChangeSignatureOrderInput,
  CreateSignatureOrderInput,
  DocumentInput,
  PadesDocumentInput,
  PadesDocumentFormInput,
  DocumentStorageMode,
  SignatureOrderStatus,
)
import pytest
import inspect
from typing import Any, cast, Coroutine

dir_path = os.path.dirname(os.path.realpath(__file__))


def getFileBytes(filename: str) -> bytes:
  with open(dir_path + os.sep + filename, "rb") as sample_file:
    return sample_file.read()


documentFixture = DocumentInput(
  pdf=PadesDocumentInput(
    title="Python sample document",
    blob=getFileBytes("sample.pdf"),
    storageMode=DocumentStorageMode.Temporary,
  )
)


async def unwrapResult[T](maybeCoroutine: T | Coroutine[Any, Any, T]) -> T:
  if inspect.iscoroutine(maybeCoroutine):
    return await maybeCoroutine
  return cast(T, maybeCoroutine)


@pytest.mark.parametrize(
  ("sdk"),
  [
    (
      CriiptoSignaturesSDKAsync(
        os.environ["CRIIPTO_SIGNATURES_CLIENT_ID"],
        os.environ["CRIIPTO_SIGNATURES_CLIENT_SECRET"],
      )
    ),
    (
      CriiptoSignaturesSDKSync(
        os.environ["CRIIPTO_SIGNATURES_CLIENT_ID"],
        os.environ["CRIIPTO_SIGNATURES_CLIENT_SECRET"],
      )
    ),
  ],
)
class TestClass:
  @pytest.mark.asyncio
  async def test_create_signature_order_add_signatory(
    self, sdk: CriiptoSignaturesSDKAsync | CriiptoSignaturesSDKSync
  ):
    signatureOrderResponse = await unwrapResult(
      sdk.createSignatureOrder(
        CreateSignatureOrderInput(
          title="Python sample signature order",
          expiresInDays=1,
          documents=[documentFixture],
        )
      )
    )

    assert signatureOrderResponse.signatureOrder
    assert signatureOrderResponse.signatureOrder.id

    signatoryResp = await unwrapResult(
      sdk.addSignatory(
        AddSignatoryInput(signatureOrderId=signatureOrderResponse.signatureOrder.id)
      )
    )

    assert signatoryResp.signatory
    assert signatoryResp.signatory.href

    await unwrapResult(
      sdk.cancelSignatureOrder(
        CancelSignatureOrderInput(
          signatureOrderId=signatureOrderResponse.signatureOrder.id
        )
      )
    )

  @pytest.mark.asyncio
  async def test_create_signature_order_with_form(
    self, sdk: CriiptoSignaturesSDKAsync | CriiptoSignaturesSDKSync
  ):
    signatureOrderResponse = await unwrapResult(
      sdk.createSignatureOrder(
        CreateSignatureOrderInput(
          title="Python sample signature order",
          expiresInDays=1,
          documents=[
            DocumentInput(
              pdf=PadesDocumentInput(
                title="Python sample document",
                blob=getFileBytes("sample-form.pdf"),
                storageMode=DocumentStorageMode.Temporary,
                form=PadesDocumentFormInput(enabled=True),
              )
            )
          ],
        )
      )
    )

    document = signatureOrderResponse.signatureOrder.documents[0]
    # TODO: This should use an auto-generated type guard, instead of an instanceof check.
    assert isinstance(
      document,
      CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_PdfDocument,
    )

    assert document.form is not None
    assert document.form.enabled

    await unwrapResult(
      sdk.cancelSignatureOrder(
        CancelSignatureOrderInput(
          signatureOrderId=signatureOrderResponse.signatureOrder.id
        )
      )
    )

  @pytest.mark.asyncio
  async def test_change_max_signatories(
    self, sdk: CriiptoSignaturesSDKAsync | CriiptoSignaturesSDKSync
  ):
    signatureOrderResponse = await unwrapResult(
      sdk.createSignatureOrder(
        CreateSignatureOrderInput(
          title="Python sample signature order",
          expiresInDays=1,
          maxSignatories=10,
          documents=[documentFixture],
        )
      )
    )

    assert signatureOrderResponse.signatureOrder
    assert signatureOrderResponse.signatureOrder.id

    changedSignatureOrderResponse = await unwrapResult(
      sdk.changeSignatureOrder(
        ChangeSignatureOrderInput(
          signatureOrderId=signatureOrderResponse.signatureOrder.id, maxSignatories=20
        )
      )
    )

    assert changedSignatureOrderResponse.signatureOrder
    assert changedSignatureOrderResponse.signatureOrder.maxSignatories == 20

    await unwrapResult(
      sdk.cancelSignatureOrder(
        CancelSignatureOrderInput(
          signatureOrderId=signatureOrderResponse.signatureOrder.id
        )
      )
    )

  @pytest.mark.asyncio
  async def test_query_signature_orders(
    self, sdk: CriiptoSignaturesSDKAsync | CriiptoSignaturesSDKSync
  ):
    title = "Python sample signature order" + str(datetime.now())

    createSignatureOrderResponse = await unwrapResult(
      sdk.createSignatureOrder(
        CreateSignatureOrderInput(
          title=title,
          expiresInDays=1,
          documents=[documentFixture],
        )
      )
    )

    signatureOrdersResponse = await unwrapResult(
      sdk.querySignatureOrders(first=1000, status=SignatureOrderStatus.OPEN)
    )

    assert isinstance(signatureOrdersResponse, QuerySignatureOrders_Viewer_Application)
    createdSignatureOrder = next(
      edge.node
      for edge in signatureOrdersResponse.signatureOrders.edges
      if edge.node.id == createSignatureOrderResponse.signatureOrder.id
    )

    assert createdSignatureOrder is not None
    assert createdSignatureOrder.title == title

    await unwrapResult(
      sdk.cancelSignatureOrder(
        CancelSignatureOrderInput(
          signatureOrderId=createSignatureOrderResponse.signatureOrder.id
        )
      )
    )
