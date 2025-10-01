from __future__ import annotations
from .utils import CustomBlobInput
from enum import StrEnum
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import RootModel
from .models import (
  CreateSignatureOrderInput,
  CleanupSignatureOrderInput,
  AddSignatoryInput,
  AddSignatoriesInput,
  ChangeSignatoryInput,
  CloseSignatureOrderInput,
  CancelSignatureOrderInput,
  SignActingAsInput,
  ValidateDocumentInput,
  ExtendSignatureOrderInput,
  DeleteSignatoryInput,
  CreateBatchSignatoryInput,
  ChangeSignatureOrderInput,
)
from .models import (
  IDScalarInput,
  IDScalarOutput,
  StringScalarInput,
  StringScalarOutput,
  BooleanScalarInput,
  BooleanScalarOutput,
  IntScalarInput,
  IntScalarOutput,
  BlobScalarInput,
  BlobScalarOutput,
  DateScalarInput,
  DateScalarOutput,
  DateTimeScalarInput,
  DateTimeScalarOutput,
  FloatScalarInput,
  FloatScalarOutput,
  URIScalarInput,
  URIScalarOutput,
)
from .models import (
  ApplicationApiKeyMode,
  DocumentIDLocation,
  DocumentStorageMode,
  EvidenceValidationStage,
  Language,
  SignatoryDocumentStatus,
  SignatoryFrontendEvent,
  SignatoryStatus,
  SignatureOrderStatus,
  VerifyApplicationEnvironment,
  WebhookInvocationEvent,
)
from gql import Client, gql
from httpx import BasicAuth
from gql.transport.httpx import HTTPXAsyncTransport, HTTPXTransport

BasicDocumentFragment = """fragment BasicDocument on Document {
  __typename
  id
  title
  reference
  ... on PdfDocument {
    documentID
    form {
      enabled
    }
  }
}"""
SignedDocumentFragment = """fragment SignedDocument on Document {
  id
  title
  blob
  signatures {
    __typename
    signatory {
      id
    }
    ... on JWTSignature {
      jwt
      jwks
      claims {
        name
        value
      }
    }
    ... on DrawableSignature {
      name
      image
    }
  }
}"""
BasicSignatoryFragment = """fragment BasicSignatory on Signatory {
  id
  status
  statusReason
  href
  downloadHref
  reference
  role
  signatureOrder {
    id
    status
    closedAt
    expiresAt
  }
  evidenceProviders {
    __typename
    id
  }
  documents {
    edges {
      status
      node {
        __typename
        id
      }
    }
  }
}"""
BasicSignatureOrderFragment = """fragment BasicSignatureOrder on SignatureOrder {
  id
  status
  title
  closedAt
  expiresAt
  maxSignatories
  signatories {
    ...BasicSignatory
  }
  evidenceProviders {
    __typename
    id
  }
}"""
BasicBatchSignatoryFragment = """fragment BasicBatchSignatory on BatchSignatory {
  id
  token
  href
}"""


class CreateSignatureOrder_CreateSignatureOrderOutput(BaseModel):
  signatureOrder: CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  documents: list[
    CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document
  ]
  evidenceProviders: list[
    CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


type CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document = (
  CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_PdfDocument
  | CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_XmlDocument
)


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory(
  BaseModel
):
  documents: CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_PdfDocument(
  BaseModel
):
  # Same value as stamped on document when using displayDocumentID
  documentID: StringScalarOutput
  form: Optional[
    CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm
  ] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_XmlDocument(
  BaseModel
):
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm(
  BaseModel
):
  enabled: BooleanScalarOutput


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class CreateSignatureOrder_CreateSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


createSignatureOrderDocument = f"""mutation createSignatureOrder($input: CreateSignatureOrderInput!) {{
  createSignatureOrder(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
      documents {{
        ...BasicDocument
      }}
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}
{BasicDocumentFragment}"""


class CleanupSignatureOrder_CleanupSignatureOrderOutput(BaseModel):
  signatureOrder: CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  documents: list[
    CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document
  ]
  evidenceProviders: list[
    CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


type CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document = (
  CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document_PdfDocument
  | CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document_XmlDocument
)


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory(
  BaseModel
):
  documents: CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document_PdfDocument(
  BaseModel
):
  # Same value as stamped on document when using displayDocumentID
  documentID: StringScalarOutput
  form: Optional[
    CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm
  ] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document_XmlDocument(
  BaseModel
):
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm(
  BaseModel
):
  enabled: BooleanScalarOutput


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class CleanupSignatureOrder_CleanupSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


cleanupSignatureOrderDocument = f"""mutation cleanupSignatureOrder($input: CleanupSignatureOrderInput!) {{
  cleanupSignatureOrder(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
      documents {{
        ...BasicDocument
      }}
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}
{BasicDocumentFragment}"""


class AddSignatory_AddSignatoryOutput(BaseModel):
  signatory: AddSignatory_AddSignatoryOutput_Signatory


class AddSignatory_AddSignatoryOutput_Signatory(BaseModel):
  documents: AddSignatory_AddSignatoryOutput_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    AddSignatory_AddSignatoryOutput_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: AddSignatory_AddSignatoryOutput_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class AddSignatory_AddSignatoryOutput_Signatory_SignatoryDocumentConnection(BaseModel):
  edges: list[
    AddSignatory_AddSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class AddSignatory_AddSignatoryOutput_Signatory_SignatureEvidenceProvider(BaseModel):
  id: IDScalarOutput


class AddSignatory_AddSignatoryOutput_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class AddSignatory_AddSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: AddSignatory_AddSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class AddSignatory_AddSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


addSignatoryDocument = f"""mutation addSignatory($input: AddSignatoryInput!) {{
  addSignatory(input: $input) {{
    signatory {{
      ...BasicSignatory
    }}
  }}
}}
{BasicSignatoryFragment}"""


class AddSignatories_AddSignatoriesOutput(BaseModel):
  signatories: list[AddSignatories_AddSignatoriesOutput_Signatory]


class AddSignatories_AddSignatoriesOutput_Signatory(BaseModel):
  documents: AddSignatories_AddSignatoriesOutput_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    AddSignatories_AddSignatoriesOutput_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: AddSignatories_AddSignatoriesOutput_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class AddSignatories_AddSignatoriesOutput_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    AddSignatories_AddSignatoriesOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class AddSignatories_AddSignatoriesOutput_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class AddSignatories_AddSignatoriesOutput_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class AddSignatories_AddSignatoriesOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: AddSignatories_AddSignatoriesOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class AddSignatories_AddSignatoriesOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


addSignatoriesDocument = f"""mutation addSignatories($input: AddSignatoriesInput!) {{
  addSignatories(input: $input) {{
    signatories {{
      ...BasicSignatory
    }}
  }}
}}
{BasicSignatoryFragment}"""


class ChangeSignatory_ChangeSignatoryOutput(BaseModel):
  signatory: ChangeSignatory_ChangeSignatoryOutput_Signatory


class ChangeSignatory_ChangeSignatoryOutput_Signatory(BaseModel):
  documents: ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class ChangeSignatory_ChangeSignatoryOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


changeSignatoryDocument = f"""mutation changeSignatory($input: ChangeSignatoryInput!) {{
  changeSignatory(input: $input) {{
    signatory {{
      ...BasicSignatory
    }}
  }}
}}
{BasicSignatoryFragment}"""


class CloseSignatureOrder_CloseSignatureOrderOutput(BaseModel):
  signatureOrder: CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  documents: list[CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document]
  evidenceProviders: list[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


type CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document = (
  CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument
)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory(BaseModel):
  documents: CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument(
  BaseModel
):
  blob: Optional[BlobScalarOutput] = Field(default=None)
  # Same value as stamped on document when using displayDocumentID
  documentID: StringScalarOutput
  form: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm
  ] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  signatures: Optional[
    list[
      CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature
    ]
  ] = Field(default=None)
  title: StringScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument(
  BaseModel
):
  blob: Optional[BlobScalarOutput] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  signatures: Optional[
    list[
      CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature
    ]
  ] = Field(default=None)
  title: StringScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm(
  BaseModel
):
  enabled: BooleanScalarOutput


type CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature = (
  CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_EmptySignature
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_JWTSignature
)

type CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature = (
  CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_EmptySignature
  | CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_JWTSignature
)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature(
  BaseModel
):
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature(
  BaseModel
):
  image: BlobScalarOutput
  name: Optional[StringScalarOutput] = Field(default=None)
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_EmptySignature(
  BaseModel
):
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_EmptySignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_JWTSignature(
  BaseModel
):
  claims: list[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_JWTClaim
  ]
  jwks: StringScalarOutput
  jwt: StringScalarOutput
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature(
  BaseModel
):
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature(
  BaseModel
):
  image: BlobScalarOutput
  name: Optional[StringScalarOutput] = Field(default=None)
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_EmptySignature(
  BaseModel
):
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_EmptySignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_JWTSignature(
  BaseModel
):
  claims: list[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_JWTClaim
  ]
  jwks: StringScalarOutput
  jwt: StringScalarOutput
  signatory: Optional[
    CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_Signatory
  ] = Field(default=None)


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_EmptySignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_JWTClaim(
  BaseModel
):
  name: StringScalarOutput
  value: StringScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_EmptySignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_JWTClaim(
  BaseModel
):
  name: StringScalarOutput
  value: StringScalarOutput


class CloseSignatureOrder_CloseSignatureOrderOutput_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


closeSignatureOrderDocument = f"""mutation closeSignatureOrder($input: CloseSignatureOrderInput!) {{
  closeSignatureOrder(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
      documents {{
        ...BasicDocument
        ...SignedDocument
      }}
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}
{BasicDocumentFragment}
{SignedDocumentFragment}"""


class CancelSignatureOrder_CancelSignatureOrderOutput(BaseModel):
  signatureOrder: CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  documents: list[
    CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document
  ]
  evidenceProviders: list[
    CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


type CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document = (
  CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document_PdfDocument
  | CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document_XmlDocument
)


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory(
  BaseModel
):
  documents: CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document_PdfDocument(
  BaseModel
):
  # Same value as stamped on document when using displayDocumentID
  documentID: StringScalarOutput
  form: Optional[
    CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm
  ] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document_XmlDocument(
  BaseModel
):
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm(
  BaseModel
):
  enabled: BooleanScalarOutput


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class CancelSignatureOrder_CancelSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


cancelSignatureOrderDocument = f"""mutation cancelSignatureOrder($input: CancelSignatureOrderInput!) {{
  cancelSignatureOrder(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
      documents {{
        ...BasicDocument
      }}
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}
{BasicDocumentFragment}"""


class SignActingAs_SignActingAsOutput(BaseModel):
  signatory: SignActingAs_SignActingAsOutput_Signatory


class SignActingAs_SignActingAsOutput_Signatory(BaseModel):
  documents: SignActingAs_SignActingAsOutput_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    SignActingAs_SignActingAsOutput_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: SignActingAs_SignActingAsOutput_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class SignActingAs_SignActingAsOutput_Signatory_SignatoryDocumentConnection(BaseModel):
  edges: list[
    SignActingAs_SignActingAsOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class SignActingAs_SignActingAsOutput_Signatory_SignatureEvidenceProvider(BaseModel):
  id: IDScalarOutput


class SignActingAs_SignActingAsOutput_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class SignActingAs_SignActingAsOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: SignActingAs_SignActingAsOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class SignActingAs_SignActingAsOutput_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


signActingAsDocument = f"""mutation signActingAs($input: SignActingAsInput!) {{
  signActingAs(input: $input) {{
    signatory {{
      ...BasicSignatory
    }}
  }}
}}
{BasicSignatoryFragment}"""


class ValidateDocument_ValidateDocumentOutput(BaseModel):
  errors: Optional[list[StringScalarOutput]] = Field(default=None)
  # Whether or not the errors are fixable using 'fixDocumentFormattingErrors'
  fixable: Optional[BooleanScalarOutput] = Field(default=None)
  valid: BooleanScalarOutput


validateDocumentDocument = """mutation validateDocument($input: ValidateDocumentInput!) {
  validateDocument(input: $input) {
    valid
    errors
    fixable
  }
}"""


class ExtendSignatureOrder_ExtendSignatureOrderOutput(BaseModel):
  signatureOrder: ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  documents: list[
    ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document
  ]
  evidenceProviders: list[
    ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


type ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document = (
  ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document_PdfDocument
  | ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document_XmlDocument
)


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory(
  BaseModel
):
  documents: ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document_PdfDocument(
  BaseModel
):
  # Same value as stamped on document when using displayDocumentID
  documentID: StringScalarOutput
  form: Optional[
    ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm
  ] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document_XmlDocument(
  BaseModel
):
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  title: StringScalarOutput


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Document_PdfDocument_PdfDocumentForm(
  BaseModel
):
  enabled: BooleanScalarOutput


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class ExtendSignatureOrder_ExtendSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


extendSignatureOrderDocument = f"""mutation extendSignatureOrder($input: ExtendSignatureOrderInput!) {{
  extendSignatureOrder(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
      documents {{
        ...BasicDocument
      }}
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}
{BasicDocumentFragment}"""


class DeleteSignatory_DeleteSignatoryOutput(BaseModel):
  signatureOrder: DeleteSignatory_DeleteSignatoryOutput_SignatureOrder


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[
    DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory(BaseModel):
  documents: DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: (
    DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatureOrder
  )
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class DeleteSignatory_DeleteSignatoryOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


deleteSignatoryDocument = f"""mutation deleteSignatory($input: DeleteSignatoryInput!) {{
  deleteSignatory(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""


class CreateBatchSignatory_CreateBatchSignatoryOutput(BaseModel):
  batchSignatory: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory(BaseModel):
  href: StringScalarOutput
  id: IDScalarOutput
  items: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem
  ]
  # The authentication token required for performing batch operations.
  token: StringScalarOutput


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem(
  BaseModel
):
  signatory: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory
  signatureOrder: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory(
  BaseModel
):
  documents: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory(
  BaseModel
):
  documents: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class CreateBatchSignatory_CreateBatchSignatoryOutput_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


createBatchSignatoryDocument = f"""mutation createBatchSignatory($input: CreateBatchSignatoryInput!) {{
  createBatchSignatory(input: $input) {{
    batchSignatory {{
      ...BasicBatchSignatory
      items {{
        signatureOrder {{
          ...BasicSignatureOrder
        }}
        signatory {{
          ...BasicSignatory
        }}
      }}
    }}
  }}
}}
{BasicBatchSignatoryFragment}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""


class ChangeSignatureOrder_ChangeSignatureOrderOutput(BaseModel):
  signatureOrder: ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[
    ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory(
  BaseModel
):
  documents: ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class ChangeSignatureOrder_ChangeSignatureOrderOutput_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


changeSignatureOrderDocument = f"""mutation changeSignatureOrder($input: ChangeSignatureOrderInput!) {{
  changeSignatureOrder(input: $input) {{
    signatureOrder {{
      ...BasicSignatureOrder
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""


class QuerySignatureOrder_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[QuerySignatureOrder_SignatureOrder_SignatureEvidenceProvider]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[QuerySignatureOrder_SignatureOrder_Signatory]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatureOrder_SignatureOrder_SignatureEvidenceProvider(BaseModel):
  id: IDScalarOutput


class QuerySignatureOrder_SignatureOrder_Signatory(BaseModel):
  documents: QuerySignatureOrder_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QuerySignatureOrder_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: QuerySignatureOrder_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatureOrder_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    QuerySignatureOrder_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QuerySignatureOrder_SignatureOrder_Signatory_SignatureEvidenceProvider(BaseModel):
  id: IDScalarOutput


class QuerySignatureOrder_SignatureOrder_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class QuerySignatureOrder_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: QuerySignatureOrder_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QuerySignatureOrder_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


querySignatureOrderDocument = f"""query signatureOrder($id: ID!) {{
  signatureOrder(id: $id) {{
    ...BasicSignatureOrder
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""


class QuerySignatureOrderWithDocuments_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  documents: list[QuerySignatureOrderWithDocuments_SignatureOrder_Document]
  evidenceProviders: list[
    QuerySignatureOrderWithDocuments_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[QuerySignatureOrderWithDocuments_SignatureOrder_Signatory]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


type QuerySignatureOrderWithDocuments_SignatureOrder_Document = (
  QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument
)


class QuerySignatureOrderWithDocuments_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Signatory(BaseModel):
  documents: QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: (
    QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatureOrder
  )
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument(BaseModel):
  blob: Optional[BlobScalarOutput] = Field(default=None)
  # Same value as stamped on document when using displayDocumentID
  documentID: StringScalarOutput
  form: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_PdfDocumentForm
  ] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  signatures: Optional[
    list[QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature]
  ] = Field(default=None)
  title: StringScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument(BaseModel):
  blob: Optional[BlobScalarOutput] = Field(default=None)
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  signatures: Optional[
    list[QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature]
  ] = Field(default=None)
  title: StringScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_PdfDocumentForm(
  BaseModel
):
  enabled: BooleanScalarOutput


type QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature = (
  QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_EmptySignature
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_JWTSignature
)

type QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature = (
  QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_EmptySignature
  | QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_JWTSignature
)


class QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature(
  BaseModel
):
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature(
  BaseModel
):
  image: BlobScalarOutput
  name: Optional[StringScalarOutput] = Field(default=None)
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_EmptySignature(
  BaseModel
):
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_EmptySignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_JWTSignature(
  BaseModel
):
  claims: list[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_JWTClaim
  ]
  jwks: StringScalarOutput
  jwt: StringScalarOutput
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature(
  BaseModel
):
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature(
  BaseModel
):
  image: BlobScalarOutput
  name: Optional[StringScalarOutput] = Field(default=None)
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_EmptySignature(
  BaseModel
):
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_EmptySignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_JWTSignature(
  BaseModel
):
  claims: list[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_JWTClaim
  ]
  jwks: StringScalarOutput
  jwt: StringScalarOutput
  signatory: Optional[
    QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_Signatory
  ] = Field(default=None)


class QuerySignatureOrderWithDocuments_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_CompositeSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_DrawableSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_EmptySignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_JWTClaim(
  BaseModel
):
  name: StringScalarOutput
  value: StringScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_PdfDocument_Signature_JWTSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_CompositeSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_DrawableSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_EmptySignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_JWTClaim(
  BaseModel
):
  name: StringScalarOutput
  value: StringScalarOutput


class QuerySignatureOrderWithDocuments_SignatureOrder_Document_XmlDocument_Signature_JWTSignature_Signatory(
  BaseModel
):
  id: IDScalarOutput


querySignatureOrderWithDocumentsDocument = f"""query signatureOrderWithDocuments($id: ID!) {{
  signatureOrder(id: $id) {{
    ...BasicSignatureOrder
    documents {{
      ...BasicDocument
      ...SignedDocument
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}
{BasicDocumentFragment}
{SignedDocumentFragment}"""


class QuerySignatory_Signatory(BaseModel):
  documents: QuerySignatory_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[QuerySignatory_Signatory_SignatureEvidenceProvider]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: QuerySignatory_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatory_Signatory_SignatoryDocumentConnection(BaseModel):
  edges: list[
    QuerySignatory_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QuerySignatory_Signatory_SignatureEvidenceProvider(BaseModel):
  id: IDScalarOutput


class QuerySignatory_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QuerySignatory_Signatory_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[QuerySignatory_Signatory_SignatureOrder_Signatory]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatory_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: (
    QuerySignatory_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  )
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QuerySignatory_Signatory_SignatureOrder_SignatureEvidenceProvider(BaseModel):
  id: IDScalarOutput


class QuerySignatory_Signatory_SignatureOrder_Signatory(BaseModel):
  documents: (
    QuerySignatory_Signatory_SignatureOrder_Signatory_SignatoryDocumentConnection
  )
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QuerySignatory_Signatory_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: QuerySignatory_Signatory_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatory_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatory_Signatory_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    QuerySignatory_Signatory_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QuerySignatory_Signatory_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatory_Signatory_SignatureOrder_Signatory_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class QuerySignatory_Signatory_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: QuerySignatory_Signatory_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QuerySignatory_Signatory_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


querySignatoryDocument = f"""query signatory($id: ID!) {{
  signatory(id: $id) {{
    signatureOrder {{
      ...BasicSignatureOrder
    }}
    ...BasicSignatory
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""
type QuerySignatureOrders_Viewer = (
  QuerySignatureOrders_Viewer_AnonymousViewer
  | QuerySignatureOrders_Viewer_Application
  | QuerySignatureOrders_Viewer_BatchSignatoryViewer
  | QuerySignatureOrders_Viewer_SignatoryViewer
  | QuerySignatureOrders_Viewer_UnvalidatedSignatoryViewer
  | QuerySignatureOrders_Viewer_UserViewer
)


class QuerySignatureOrders_Viewer_AnonymousViewer(BaseModel):
  pass


class QuerySignatureOrders_Viewer_Application(BaseModel):
  signatureOrders: QuerySignatureOrders_Viewer_Application_SignatureOrderConnection


class QuerySignatureOrders_Viewer_BatchSignatoryViewer(BaseModel):
  pass


class QuerySignatureOrders_Viewer_SignatoryViewer(BaseModel):
  pass


class QuerySignatureOrders_Viewer_UnvalidatedSignatoryViewer(BaseModel):
  pass


class QuerySignatureOrders_Viewer_UserViewer(BaseModel):
  pass


# A connection from an object to a list of objects of type SignatureOrder
class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection(BaseModel):
  # Information to aid in pagination.
  edges: list[
    QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge
  ]


# An edge in a connection from an object to another object of type SignatureOrder
class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge(
  BaseModel
):
  # The item at the end of the edge. Must NOT be an enumerable collection.
  node: QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory(
  BaseModel
):
  documents: QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QuerySignatureOrders_Viewer_Application_SignatureOrderConnection_SignatureOrderEdge_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


querySignatureOrdersDocument = f"""query signatureOrders($status: SignatureOrderStatus, $first: Int!, $after: String) {{
  viewer {{
    __typename
    ... on Application {{
      signatureOrders(status: $status, first: $first, after: $after) {{
        edges {{
          node {{
            ...BasicSignatureOrder
          }}
        }}
      }}
    }}
  }}
}}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""


class QueryBatchSignatory_BatchSignatory(BaseModel):
  href: StringScalarOutput
  id: IDScalarOutput
  items: list[QueryBatchSignatory_BatchSignatory_BatchSignatoryItem]
  # The authentication token required for performing batch operations.
  token: StringScalarOutput


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem(BaseModel):
  signatory: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory
  signatureOrder: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory(BaseModel):
  documents: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: (
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatureOrder
  )
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder(BaseModel):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_SignatureEvidenceProvider
  ]
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  # Number of max signatories for the signature order
  maxSignatories: IntScalarOutput
  # List of signatories for the signature order.
  signatories: list[
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory
  ]
  status: SignatureOrderStatus
  title: Optional[StringScalarOutput] = Field(default=None)


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory(
  BaseModel
):
  documents: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection
  # A download link for signatories to download their signed documents. Signatories must verify their identity before downloading. Can be used when signature order is closed with document retention.
  downloadHref: Optional[StringScalarOutput] = Field(default=None)
  evidenceProviders: list[
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureEvidenceProvider
  ]
  # A link to the signatures frontend, you can send this link to your users to enable them to sign your documents.
  href: StringScalarOutput
  id: IDScalarOutput
  reference: Optional[StringScalarOutput] = Field(default=None)
  role: Optional[StringScalarOutput] = Field(default=None)
  # Signature order for the signatory.
  signatureOrder: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureOrder
  # The current status of the signatory.
  status: SignatoryStatus
  # The reason for the signatory status (rejection reason when rejected).
  statusReason: Optional[StringScalarOutput] = Field(default=None)


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection(
  BaseModel
):
  edges: list[
    QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge
  ]


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureEvidenceProvider(
  BaseModel
):
  id: IDScalarOutput


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatureOrder(
  BaseModel
):
  closedAt: Optional[DateTimeScalarOutput] = Field(default=None)
  expiresAt: DateTimeScalarOutput
  id: IDScalarOutput
  status: SignatureOrderStatus


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge(
  BaseModel
):
  node: QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document
  status: Optional[SignatoryDocumentStatus] = Field(default=None)


class QueryBatchSignatory_BatchSignatory_BatchSignatoryItem_SignatureOrder_Signatory_SignatoryDocumentConnection_SignatoryDocumentEdge_Document(
  BaseModel
):
  id: IDScalarOutput


queryBatchSignatoryDocument = f"""query batchSignatory($id: ID!) {{
  batchSignatory(id: $id) {{
    ...BasicBatchSignatory
    items {{
      signatureOrder {{
        ...BasicSignatureOrder
      }}
      signatory {{
        ...BasicSignatory
      }}
    }}
  }}
}}
{BasicBatchSignatoryFragment}
{BasicSignatureOrderFragment}
{BasicSignatoryFragment}"""


class CriiptoSignaturesSDKAsync:
  def __init__(self, clientId: str, clientSecret: str):
    auth = BasicAuth(username=clientId, password=clientSecret)
    headers = {"Criipto-Sdk": "criipto-signatures-python"}
    transport = HTTPXAsyncTransport(
      url="https://signatures-api.criipto.com/v1/graphql", auth=auth, headers=headers
    )
    self.client = Client(transport=transport, fetch_schema_from_transport=False)

  async def createSignatureOrder(
    self, input: CreateSignatureOrderInput
  ) -> CreateSignatureOrder_CreateSignatureOrderOutput:
    query = gql(createSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[CreateSignatureOrder_CreateSignatureOrderOutput]
      .model_validate(result.get("createSignatureOrder"))
      .root
    )
    return parsed

  async def cleanupSignatureOrder(
    self, input: CleanupSignatureOrderInput
  ) -> CleanupSignatureOrder_CleanupSignatureOrderOutput:
    query = gql(cleanupSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[CleanupSignatureOrder_CleanupSignatureOrderOutput]
      .model_validate(result.get("cleanupSignatureOrder"))
      .root
    )
    return parsed

  async def addSignatory(
    self, input: AddSignatoryInput
  ) -> AddSignatory_AddSignatoryOutput:
    query = gql(addSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[AddSignatory_AddSignatoryOutput]
      .model_validate(result.get("addSignatory"))
      .root
    )
    return parsed

  async def addSignatories(
    self, input: AddSignatoriesInput
  ) -> AddSignatories_AddSignatoriesOutput:
    query = gql(addSignatoriesDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[AddSignatories_AddSignatoriesOutput]
      .model_validate(result.get("addSignatories"))
      .root
    )
    return parsed

  async def changeSignatory(
    self, input: ChangeSignatoryInput
  ) -> ChangeSignatory_ChangeSignatoryOutput:
    query = gql(changeSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[ChangeSignatory_ChangeSignatoryOutput]
      .model_validate(result.get("changeSignatory"))
      .root
    )
    return parsed

  async def closeSignatureOrder(
    self, input: CloseSignatureOrderInput
  ) -> CloseSignatureOrder_CloseSignatureOrderOutput:
    query = gql(closeSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[CloseSignatureOrder_CloseSignatureOrderOutput]
      .model_validate(result.get("closeSignatureOrder"))
      .root
    )
    return parsed

  async def cancelSignatureOrder(
    self, input: CancelSignatureOrderInput
  ) -> CancelSignatureOrder_CancelSignatureOrderOutput:
    query = gql(cancelSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[CancelSignatureOrder_CancelSignatureOrderOutput]
      .model_validate(result.get("cancelSignatureOrder"))
      .root
    )
    return parsed

  async def signActingAs(
    self, input: SignActingAsInput
  ) -> SignActingAs_SignActingAsOutput:
    query = gql(signActingAsDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[SignActingAs_SignActingAsOutput]
      .model_validate(result.get("signActingAs"))
      .root
    )
    return parsed

  async def validateDocument(
    self, input: ValidateDocumentInput
  ) -> ValidateDocument_ValidateDocumentOutput:
    query = gql(validateDocumentDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[ValidateDocument_ValidateDocumentOutput]
      .model_validate(result.get("validateDocument"))
      .root
    )
    return parsed

  async def extendSignatureOrder(
    self, input: ExtendSignatureOrderInput
  ) -> ExtendSignatureOrder_ExtendSignatureOrderOutput:
    query = gql(extendSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[ExtendSignatureOrder_ExtendSignatureOrderOutput]
      .model_validate(result.get("extendSignatureOrder"))
      .root
    )
    return parsed

  async def deleteSignatory(
    self, input: DeleteSignatoryInput
  ) -> DeleteSignatory_DeleteSignatoryOutput:
    query = gql(deleteSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[DeleteSignatory_DeleteSignatoryOutput]
      .model_validate(result.get("deleteSignatory"))
      .root
    )
    return parsed

  async def createBatchSignatory(
    self, input: CreateBatchSignatoryInput
  ) -> CreateBatchSignatory_CreateBatchSignatoryOutput:
    query = gql(createBatchSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[CreateBatchSignatory_CreateBatchSignatoryOutput]
      .model_validate(result.get("createBatchSignatory"))
      .root
    )
    return parsed

  async def changeSignatureOrder(
    self, input: ChangeSignatureOrderInput
  ) -> ChangeSignatureOrder_ChangeSignatureOrderOutput:
    query = gql(changeSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[ChangeSignatureOrder_ChangeSignatureOrderOutput]
      .model_validate(result.get("changeSignatureOrder"))
      .root
    )
    return parsed

  async def querySignatureOrder(
    self, id: IDScalarInput
  ) -> QuerySignatureOrder_SignatureOrder:
    query = gql(querySignatureOrderDocument)
    query.variable_values = {"id": id}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[QuerySignatureOrder_SignatureOrder]
      .model_validate(result.get("signatureOrder"))
      .root
    )
    return parsed

  async def querySignatureOrderWithDocuments(
    self, id: IDScalarInput
  ) -> QuerySignatureOrderWithDocuments_SignatureOrder:
    query = gql(querySignatureOrderWithDocumentsDocument)
    query.variable_values = {"id": id}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[QuerySignatureOrderWithDocuments_SignatureOrder]
      .model_validate(result.get("signatureOrder"))
      .root
    )
    return parsed

  async def querySignatory(self, id: IDScalarInput) -> QuerySignatory_Signatory:
    query = gql(querySignatoryDocument)
    query.variable_values = {"id": id}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[QuerySignatory_Signatory].model_validate(result.get("signatory")).root
    )
    return parsed

  async def querySignatureOrders(
    self,
    first: IntScalarInput,
    status: Optional[SignatureOrderStatus] = None,
    after: Optional[StringScalarInput] = None,
  ) -> QuerySignatureOrders_Viewer:
    query = gql(querySignatureOrdersDocument)
    query.variable_values = {
      "first": first,
      "status": status if status is not None else "",
      "after": after,
    }
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[QuerySignatureOrders_Viewer].model_validate(result.get("viewer")).root
    )
    return parsed

  async def queryBatchSignatory(
    self, id: IDScalarInput
  ) -> QueryBatchSignatory_BatchSignatory:
    query = gql(queryBatchSignatoryDocument)
    query.variable_values = {"id": id}
    result = await self.client.execute_async(query)
    parsed = (
      RootModel[QueryBatchSignatory_BatchSignatory]
      .model_validate(result.get("batchSignatory"))
      .root
    )
    return parsed


class CriiptoSignaturesSDKSync:
  def __init__(self, clientId: str, clientSecret: str):
    auth = BasicAuth(username=clientId, password=clientSecret)
    headers = {"Criipto-Sdk": "criipto-signatures-python"}
    transport = HTTPXTransport(
      url="https://signatures-api.criipto.com/v1/graphql", auth=auth, headers=headers
    )
    self.client = Client(transport=transport, fetch_schema_from_transport=False)

  def createSignatureOrder(
    self, input: CreateSignatureOrderInput
  ) -> CreateSignatureOrder_CreateSignatureOrderOutput:
    query = gql(createSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[CreateSignatureOrder_CreateSignatureOrderOutput]
      .model_validate(result.get("createSignatureOrder"))
      .root
    )
    return parsed

  def cleanupSignatureOrder(
    self, input: CleanupSignatureOrderInput
  ) -> CleanupSignatureOrder_CleanupSignatureOrderOutput:
    query = gql(cleanupSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[CleanupSignatureOrder_CleanupSignatureOrderOutput]
      .model_validate(result.get("cleanupSignatureOrder"))
      .root
    )
    return parsed

  def addSignatory(self, input: AddSignatoryInput) -> AddSignatory_AddSignatoryOutput:
    query = gql(addSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[AddSignatory_AddSignatoryOutput]
      .model_validate(result.get("addSignatory"))
      .root
    )
    return parsed

  def addSignatories(
    self, input: AddSignatoriesInput
  ) -> AddSignatories_AddSignatoriesOutput:
    query = gql(addSignatoriesDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[AddSignatories_AddSignatoriesOutput]
      .model_validate(result.get("addSignatories"))
      .root
    )
    return parsed

  def changeSignatory(
    self, input: ChangeSignatoryInput
  ) -> ChangeSignatory_ChangeSignatoryOutput:
    query = gql(changeSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[ChangeSignatory_ChangeSignatoryOutput]
      .model_validate(result.get("changeSignatory"))
      .root
    )
    return parsed

  def closeSignatureOrder(
    self, input: CloseSignatureOrderInput
  ) -> CloseSignatureOrder_CloseSignatureOrderOutput:
    query = gql(closeSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[CloseSignatureOrder_CloseSignatureOrderOutput]
      .model_validate(result.get("closeSignatureOrder"))
      .root
    )
    return parsed

  def cancelSignatureOrder(
    self, input: CancelSignatureOrderInput
  ) -> CancelSignatureOrder_CancelSignatureOrderOutput:
    query = gql(cancelSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[CancelSignatureOrder_CancelSignatureOrderOutput]
      .model_validate(result.get("cancelSignatureOrder"))
      .root
    )
    return parsed

  def signActingAs(self, input: SignActingAsInput) -> SignActingAs_SignActingAsOutput:
    query = gql(signActingAsDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[SignActingAs_SignActingAsOutput]
      .model_validate(result.get("signActingAs"))
      .root
    )
    return parsed

  def validateDocument(
    self, input: ValidateDocumentInput
  ) -> ValidateDocument_ValidateDocumentOutput:
    query = gql(validateDocumentDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[ValidateDocument_ValidateDocumentOutput]
      .model_validate(result.get("validateDocument"))
      .root
    )
    return parsed

  def extendSignatureOrder(
    self, input: ExtendSignatureOrderInput
  ) -> ExtendSignatureOrder_ExtendSignatureOrderOutput:
    query = gql(extendSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[ExtendSignatureOrder_ExtendSignatureOrderOutput]
      .model_validate(result.get("extendSignatureOrder"))
      .root
    )
    return parsed

  def deleteSignatory(
    self, input: DeleteSignatoryInput
  ) -> DeleteSignatory_DeleteSignatoryOutput:
    query = gql(deleteSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[DeleteSignatory_DeleteSignatoryOutput]
      .model_validate(result.get("deleteSignatory"))
      .root
    )
    return parsed

  def createBatchSignatory(
    self, input: CreateBatchSignatoryInput
  ) -> CreateBatchSignatory_CreateBatchSignatoryOutput:
    query = gql(createBatchSignatoryDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[CreateBatchSignatory_CreateBatchSignatoryOutput]
      .model_validate(result.get("createBatchSignatory"))
      .root
    )
    return parsed

  def changeSignatureOrder(
    self, input: ChangeSignatureOrderInput
  ) -> ChangeSignatureOrder_ChangeSignatureOrderOutput:
    query = gql(changeSignatureOrderDocument)
    query.variable_values = {"input": input.model_dump()}
    result = self.client.execute(query)
    parsed = (
      RootModel[ChangeSignatureOrder_ChangeSignatureOrderOutput]
      .model_validate(result.get("changeSignatureOrder"))
      .root
    )
    return parsed

  def querySignatureOrder(
    self, id: IDScalarInput
  ) -> QuerySignatureOrder_SignatureOrder:
    query = gql(querySignatureOrderDocument)
    query.variable_values = {"id": id}
    result = self.client.execute(query)
    parsed = (
      RootModel[QuerySignatureOrder_SignatureOrder]
      .model_validate(result.get("signatureOrder"))
      .root
    )
    return parsed

  def querySignatureOrderWithDocuments(
    self, id: IDScalarInput
  ) -> QuerySignatureOrderWithDocuments_SignatureOrder:
    query = gql(querySignatureOrderWithDocumentsDocument)
    query.variable_values = {"id": id}
    result = self.client.execute(query)
    parsed = (
      RootModel[QuerySignatureOrderWithDocuments_SignatureOrder]
      .model_validate(result.get("signatureOrder"))
      .root
    )
    return parsed

  def querySignatory(self, id: IDScalarInput) -> QuerySignatory_Signatory:
    query = gql(querySignatoryDocument)
    query.variable_values = {"id": id}
    result = self.client.execute(query)
    parsed = (
      RootModel[QuerySignatory_Signatory].model_validate(result.get("signatory")).root
    )
    return parsed

  def querySignatureOrders(
    self,
    first: IntScalarInput,
    status: Optional[SignatureOrderStatus] = None,
    after: Optional[StringScalarInput] = None,
  ) -> QuerySignatureOrders_Viewer:
    query = gql(querySignatureOrdersDocument)
    query.variable_values = {
      "first": first,
      "status": status if status is not None else "",
      "after": after,
    }
    result = self.client.execute(query)
    parsed = (
      RootModel[QuerySignatureOrders_Viewer].model_validate(result.get("viewer")).root
    )
    return parsed

  def queryBatchSignatory(
    self, id: IDScalarInput
  ) -> QueryBatchSignatory_BatchSignatory:
    query = gql(queryBatchSignatoryDocument)
    query.variable_values = {"id": id}
    result = self.client.execute(query)
    parsed = (
      RootModel[QueryBatchSignatory_BatchSignatory]
      .model_validate(result.get("batchSignatory"))
      .root
    )
    return parsed
