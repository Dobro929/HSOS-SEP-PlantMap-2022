import type { Bed } from "@/types/bed";

export interface LeafletMapRef {
  createMarker(bed: Bed): void;
  flyToAndOpenPopup(id: number, latitude: number, longitude: number): void;
}
