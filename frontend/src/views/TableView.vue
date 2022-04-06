<template>
  <div class="table-container py-3 px-4">
    <div class="table-wrapper">
      <table class="table table-borderless">
        <thead>
          <tr>
            <td>Id</td>
            <td>Name</td>
            <td>Culture</td>
            <td>Latitude</td>
            <td>Longitude</td>
          </tr>
        </thead>
        <tbody>
          <tr
            v-bind:key="bed"
            v-for="bed in beds"
            v-on:click="goToMap(bed.id, bed.latitude, bed.longitude)"
          >
            <td>{{ bed.id }}</td>
            <td>{{ bed.name }}</td>
            <td>{{ bed.culture }}</td>
            <td>{{ bed.latitude }}</td>
            <td>{{ bed.longitude }}</td>
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
