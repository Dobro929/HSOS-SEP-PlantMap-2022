import { createRouter, createWebHistory } from "vue-router";
import TableView from "../views/TableView.vue";
import MapView from "@/views/MapView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/table",
    },
    {
      path: "/table",
      name: "table",
      component: TableView,
    },
    {
      path: "/map",
      name: "map",
      component: MapView,
    },
  ],
});

export default router;
