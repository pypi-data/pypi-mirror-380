from pydantic import BaseModel
from dataclasses import field

from open_mpic_core.common_domain.enum.regional_internet_registry import RegionalInternetRegistry


class RemotePerspective(BaseModel):
    code: str  # example: "us-west-2"
    name: str | None = None  # example: "US West (Oregon)" (optional)
    rir: RegionalInternetRegistry  # example: "RegionalInternetRegistry.ARIN"
    too_close_codes: list[str] | None = field(default_factory=list)  # example: ["us-west-1", "us-west-2"]

    def is_perspective_too_close(self, perspective):
        return perspective.code in self.too_close_codes
