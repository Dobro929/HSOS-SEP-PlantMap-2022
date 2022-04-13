import { defineStore } from "pinia";
import { getBedDetail, getBeds } from "@/service/bedApi";
import type { Bed } from "@/types/bed";

export const BedStore = defineStore({
  id: "beds",
  state: () => ({
    beds: [] as Bed[],
  }),
  getters: {
    getBeds(): Bed[] {
      return this.beds || [];
    },
  },
  actions: {
    async setStoreDataFromApi() {
      this.beds = (await getBeds()).beds;

      for (const bedID in this.beds) {
        const bed_detail: Bed = (await getBedDetail(this.beds[bedID].uuid)).bed;        
        if (bed_detail) {
          this.beds[bedID] = bed_detail;
        }
      }      
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
