<template>
  <div class="table-container py-3 px-4">
    <div class="table-wrapper">
      <table class="table table-borderless">
        <thead>
          <tr v-if="beds">
            <td>Name</td>
            <td>Latitude</td>
            <td>Longitude</td>          
            <td>Kultur</td>
            <td>Status</td>
          </tr>
        </thead>
        <tbody>
          <tr
            v-bind:key="bed"
            v-for="bed in beds"
            v-on:click="goToMap(bed.uuid, bed.geolocation.latitude, bed.geolocation.longitude)"
          >
            <td>{{ bed.name }}</td>
            <template v-if="bed.geolocation">
              <td>{{ bed.geolocation.latitude }}</td>
              <td>{{ bed.geolocation.longitude }}</td>
            </template>
            <template v-else>
            <td>-</td>
            <td>-</td>
            </template>
            <td>Tomaten</td>
            <td>
            <span class="badge bg-good">Sehr gut</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { BedStore } from "@/stores/bedStore";
import { storeToRefs } from "pinia";
import type { Ref } from "vue";
import type { Bed } from "@/types/bed";

export default defineComponent({
  name: "TableView",
  setup() {
    const main = BedStore();
    const beds: Ref<Bed[]> = storeToRefs(main).beds;
    
    return {
      beds,
    };
  },
  methods: {
    goToMap(id: number, latitude: number, longitude: number): void {
      this.$router.push({
        name: "map",
        params: { id: id, latitude: latitude, longitude: longitude },
      });
    },
  },
});
</script>

<style scoped lang="scss">
.table-container {
  overflow-y: auto;
  width: 100%;
  .table-wrapper {
    border-radius: 1rem;
    padding: 10px;
    box-shadow: 0 5px 20px #97979721;
    width: fit-content;
    table {
      margin-bottom: 0;
      color: #2f2f2f;
      thead {
        font-weight: 600;
        tr {
          td {
            padding: 0.5rem 1rem;
            font-weight: 600;
          }
        }
      }
      tbody {
        tr {
          td {
            padding: 0.5rem 1rem;

            .bg-good {
              background-color: #79b729;
            }
          }
          & td:first-child {
            border-radius: 1rem 0 0 1rem;
          }
          & td:last-child {
            border-radius: 0 1rem 1rem 0;
          }
          &:hover {
            cursor: pointer;
            color: white;
            td {
              background: #79b729;
              box-shadow: 0 5px 20px #97979721;
            }
          }
        }
      }
    }
  }
}
</style>
