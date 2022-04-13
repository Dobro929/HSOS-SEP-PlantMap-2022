<template>
  <div class="map-container">
    <div id="map"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import L from "leaflet";
import type { Bed } from "@/types/bed";

const greenIcon: L.Icon = new L.Icon({
  iconUrl: "src/assets/marker/marker_green.svg",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41],
});

export default defineComponent({
  name: "LeafletMap",
  setup() {
    let leafletMap = {} as L.Map;
    let markers = new Map<number, L.Marker>();
    return {
      leafletMap,
      markers,
    };
  },
  mounted() {
    this.leafletMap = L.map("map", { zoomControl: false }).setView(
      new L.LatLng(52.27264, 8.0498),
      13
    );
    L.tileLayer(
      "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
      {
        attribution:
          'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 20,
        id: "sadsadas/cl1jkmk1a002v15mx9pc8koka",
        tileSize: 512,
        zoomOffset: -1,
        accessToken:
          "pk.eyJ1Ijoic2Fkc2FkYXMiLCJhIjoiY2wxZGZzZnM1MGhjOTNibzJydmlpdmNtZiJ9.gPB9KNmTlEDMDFNGKBfcug",
      }
    ).addTo(this.leafletMap);
  },
  methods: {
    createMarker(bed: Bed): void {
      let marker: L.Marker = L.marker(
        [bed.geolocation.latitude, bed.geolocation.longitude],
        {
          icon: greenIcon,
        }
      ).addTo(this.leafletMap);
      this.markers.set(bed.uuid, marker);
      this.addBedPopupToMarker(marker, bed);
    },
    flyToAndOpenPopup(id: number, latitude: number, longitude: number): void {
      this.leafletMap.flyTo(new L.LatLng(latitude, longitude), 20, {
        animate: true,
        duration: 2.0,
      });
      const marker = this.markers.get(id);
      if (marker) {
        marker.openPopup();
      }
    },
    addBedPopupToMarker(marker: L.Marker, bed: Bed): void {
      let popup: L.Popup = L.popup({ className: "bed-popup" }).setContent(
        "<h1>" +
          bed.name +
          "</h1>" +
          "<table>" +
          "<tr>" +
          "<th>Info:</th>" +
          "<td>Hier steht ein Info</td>" +
          "</tr>" +
          "<tr>" +
          "</table>"
      );
      marker.bindPopup(popup);
    },
  },
});
</script>

<style lang="scss">
.map-container {
  width: 100%;
}
#map {
  height: 100vh;
  width: 100%;
  background-color: #282827;

  .leaflet-control-container {
    height: 100vh;
  }

  .bed-popup {
    h1 {
      font-size: 16px;
      font-weight: 600;
      margin: 5px 0 10px;
      padding: 0;
      color: #2f2f2f;
    }

    table {
      border-collapse: separate;
      border-spacing: 0 5px;
      color: #2f2f2f;

      th {
        padding-right: 5px !important;
      }

      td,
      th {
        font-size: 12px;
        padding: 0;
      }
    }
  }
}
</style>
