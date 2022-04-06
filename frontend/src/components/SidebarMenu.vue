<template>
  <div class="sidebar d-flex flex-column flex-shrink-0" style="width: 5rem">
    <router-link to="/" class="img-wrapper">
      <img src="@/assets/img/logo_small.svg" alt="Logo" />
    </router-link>
    <ul class="nav nav-pills nav-flush flex-column mb-auto text-center">
      <router-link to="/table" custom v-slot="{ href, navigate, isActive }">
        <li class="nav-item">
          <a
            class="nav-link"
            v-bind:class="{ active: isActive }"
            :href="href"
            @click="navigate"
            ><font-awesome-icon icon="table"
          /></a>
        </li>
      </router-link>
      <router-link to="/map" custom v-slot="{ href, navigate, isActive }">
        <li class="nav-item">
          <a
            class="nav-link"
            v-bind:class="{ active: isActive }"
            :href="href"
            @click="navigate"
            ><font-awesome-icon icon="map"
          /></a>
        </li>
      </router-link>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

export default defineComponent({
  name: "SidebarMenu",
  components: {
    FontAwesomeIcon,
  },
});
</script>

<style scoped lang="scss">
.sidebar {
  background-color: $primary;
  box-shadow: 5px 0 40px #24252222;
  padding: 2rem 0;
  .img-wrapper {
    margin: 0 auto;
    img {
      width: 3rem;
    }
  }
  .nav {
    margin-top: 2rem;
    li {
      padding: 5px 0;
      width: 3.5rem;
      margin: 0 auto;
      a {
        color: white;
        padding: 1rem 0;
        border-radius: 1rem;
        transition: all 250ms ease-in-out;

        &:hover {
          color: $primary;
          background-color: white;
          box-shadow: 5px 0 40px #24252222;
        }
      }
      .active {
        color: $primary;
        background-color: white;
        box-shadow: 5px 0 40px #24252222;
      }
    }
  }
}
</style>
