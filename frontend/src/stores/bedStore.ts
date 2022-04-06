import { defineStore } from "pinia";
import { getBedDetail, getBeds } from "@/service/bedApi";
import type { Bed } from "@/types/bed";

export const BedStore = defineStore({
  id: "beds",
  state: () => ({
    bedIds: [] as string[],
    beds: [] as Bed[],
  }),
  getters: {
    getBeds(): Bed[] {
      return this.beds || [];
    },
  },
  actions: {
    async setStoreDataFromApi() {
      this.bedIds = (await getBeds()).beds;
      const bedArray: Bed[] = [];
      for (const bedID in this.bedIds) {
        const bed = await getBedDetail(bedID);
        if (bed) {
          bedArray.push(bed);
        }
      }
      this.beds = bedArray;
    },
    /*async getBedIds() {
      this.bedIds = (await getBeds()).beds;
    },
    async getBedDetails() {
      const bedArray: Bed[] = [];
      for (const bedID in this.bedIds) {
        const bed = await getBedDetail(bedID);
        if (bed) {
          bedArray.push(bed);
        }
      }
      this.beds = bedArray;
    },*/
  },
});
