from enum import StrEnum
from typing import Annotated

from pydantic import AfterValidator, BaseModel

from mmar_mapi.file_storage import ResourceId
from mmar_mapi.models.chat import Chat, ChatMessage
from mmar_mapi.models.tracks import DomainInfo, TrackInfo

Value = str
Interpretation = str


class ChatManagerAPI:
    def get_domains(self, *, client_id: str, language_code: str = "ru") -> list[DomainInfo]:
        raise NotImplementedError

    def get_tracks(self, *, client_id: str, language_code: str = "ru") -> list[TrackInfo]:
        raise NotImplementedError

    def get_response(self, *, chat: Chat) -> list[ChatMessage]:
        raise NotImplementedError


class TextGeneratorAPI:
    def process(self, *, chat: Chat) -> str:
        raise NotImplementedError


class ContentInterpreterRemoteResponse(BaseModel):
    interpretation: str
    resource_fname: str
    resource: bytes


class ContentInterpreterRemoteAPI:
    def interpret_remote(
        self, *, kind: str, query: str, resource: bytes, chat: Chat | None = None
    ) -> ContentInterpreterRemoteResponse:
        raise NotImplementedError


class ClassifierAPI:
    def get_values(self) -> list[Value]:
        raise NotImplementedError

    def evaluate(self, *, chat: Chat) -> Value:
        raise NotImplementedError


class CriticAPI:
    def evaluate(self, *, text: str, chat: Chat | None = None) -> float:
        raise NotImplementedError


class ContentInterpreterAPI:
    def interpret(
        self, *, kind: str, query: str, resource_id: str = "", chat: Chat | None = None
    ) -> tuple[Interpretation, ResourceId | None]:
        raise NotImplementedError


class TextProcessorAPI:
    def process(self, *, text: str, chat: Chat | None = None) -> str:
        raise NotImplementedError


class TextExtractorAPI:
    def extract(self, *, resource_id: ResourceId) -> ResourceId:
        """returns file with text"""
        raise NotImplementedError


PageRange = Annotated[tuple[int, int], AfterValidator(lambda rng: rng[0] <= rng[1])]
ForceOCR = StrEnum("ForceOCR", ["ENABLED", "DISABLED", "AUTO"])
OutputType = StrEnum("OutputType", ["RAW", "PLAIN", "MARKDOWN"])


class DocExtractionSpec(BaseModel):
    page_range: PageRange | None = None
    output_type: OutputType = OutputType.MARKDOWN
    force_ocr: ForceOCR = ForceOCR.AUTO
    do_ocr: bool = False
    do_table_structure: bool = False
    do_cell_matching: bool = False
    do_annotations: bool = False
    do_image_extraction: bool = False
    generate_page_images: bool = False
    images_scale: float = 2.0

    def _update(self, **update):
        return self.model_copy(update=update)

    # fmt: off
    def with_output_type_raw(self): return self._update(output_type=OutputType.RAW)
    def with_output_type_plain(self): return self._update(output_type=OutputType.PLAIN)
    def with_ocr(self): return self._update(do_ocr=True)
    def with_tables(self): return self._update(do_table_structure=True, do_cell_matching=True)
    def with_images(self): return self._update(do_image_extraction=True)
    def with_annotations(self): return self._update(do_annotations=True)
    def with_force_ocr_enabled(self): return self._update(force_ocr=ForceOCR.ENABLED)
    def with_force_ocr_disabled(self): return self._update(force_ocr=ForceOCR.DISABLED)
    def with_page_images(self): return self._update(generate_page_images=True)
    def with_page_range(self, page_range: PageRange): return self._update(page_range=page_range)
    # fmt: on


class ExtractedImage(BaseModel):
    page: int
    image_resource_id: ResourceId | None = None


class ExtractedImageMetadata(BaseModel):
    annotation: str = ""
    caption: str = ""
    width: int | None = None
    height: int | None = None


class ExtractedPicture(ExtractedImage, ExtractedImageMetadata):
    pass


class ExtractedTable(ExtractedImage, ExtractedImageMetadata):
    formatted_str: str


class ExtractedPageImage(ExtractedImage):
    pass


class DocExtractionOutput(BaseModel):
    config: DocExtractionSpec
    text: str = ""
    tables: list[ExtractedTable] = []
    pictures: list[ExtractedPicture] = []
    page_images: list[ExtractedPageImage] = []


class DocumentExtractorAPI:
    def extract(self, *, resource_id: ResourceId, spec: DocExtractionSpec) -> ResourceId:
        """returns file with DocExtractionOutput"""
        raise NotImplementedError
