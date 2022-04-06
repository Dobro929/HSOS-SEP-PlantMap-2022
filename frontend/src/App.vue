<template>
  <main>
    <SidebarMenu></SidebarMenu>
    <RouterView />
  </main>
</template>

<script lang="ts">
import SidebarMenu from "@/components/SidebarMenu.vue";
import { defineComponent } from "vue";
import { BedStore } from "@/stores/bedStore";

export default defineComponent({
  name: "App",
  components: {
    SidebarMenu,
  },
  mounted() {
    const main = BedStore();
    main.setStoreDataFromApi();
  },
});
</script>

<style lang="scss">
main {
  display: flex;
  flex-wrap: nowrap;
  height: 100vh;
  max-height: 100vh;
  overflow-x: auto;
  overflow-y: hidden;
  background-color: white;
}
</style>
