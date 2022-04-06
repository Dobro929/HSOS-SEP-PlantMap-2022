<template>
  <LeafletMap ref="map"></LeafletMap>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { BedStore } from "@/stores/bedStore";
import { storeToRefs } from "pinia";
import type { Ref } from "vue";
import type { Bed } from "@/types/bed";
import LeafletMap from "@/components/LeafletMap.vue";
import type { LeafletMapRef } from "@/types/interfaces/leafletMapRef";

export default defineComponent({
  name: "MapView",
  components: {
    LeafletMap,
  },
  setup() {
    const main = BedStore();
    const beds: Ref<Bed[]> = storeToRefs(main).beds;
    let map = {} as LeafletMapRef; //not the best solution

    return {
      beds,
      map,
    };
  },
  mounted() {
    this.map = this.$refs.map as LeafletMapRef;
    this.createMapMarker();

    if (
      this.$route.params.id &&
      this.$route.params.latitude &&
      this.$route.params.longitude
    ) {
      this.map.flyToAndOpenPopup(
        Number(this.$route.params.id),
        Number(this.$route.params.latitude),
        Number(this.$route.params.longitude)
      );
    }
  },
  methods: {
    createMapMarker(): void {
      this.beds.forEach((bed) => {
        this.map.createMarker(bed);
      });
    },
  },
});
</script>

<style scoped lang="scss"></style>
