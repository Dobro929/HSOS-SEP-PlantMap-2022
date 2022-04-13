export interface DemoBed {
  id: number;
  name: string;
  culture: string;
  longitude: number;
  latitude: number;
}

export interface Geolocation {
  coordinateSystem: string;
  ellipsoid: string;
  latitude: number;
  longitude: number;
}

export interface Geometrie {
  name: string;
  uuid: string;
  type: string;
  frameId: string;
  stamp: string;
}

export interface Bed {
  uuid: string;
  name: string;
  geolocation: Geolocation;
  geometries: Geometrie[]
}