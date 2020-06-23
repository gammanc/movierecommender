<template>
  <v-app>
    <v-app-bar app color="black" class="px-10">
      <div class="d-flex align-center">
        <v-icon>movie</v-icon>
        <span
          class="ml-2 text-button font-weight-bold"
          style="color: rgba(255, 255, 255, 0.54)"
          >MOVIE RECOMMENDER</span
        >
      </div>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/" target="_blank" icon>
        <v-icon>mdi-github</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content class="px-12">
      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>
