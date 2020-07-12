<template>
  <v-app height="">
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
   <v-carousel
      cycle
      height="752px"
      hide-delimiter-background
                :show-arrows="false"
    >
        <v-carousel-item
          v-for="(slide, i) in slides"
          :key="i"
        >
          <v-sheet
            :color="colors[i]"
            height="100%"
          >
            <v-row
            class ="fill-height"
              align="center"
              justify="center"
            >
              <div class="display-3">{{ slide }} Slide</div>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    <v-content class="px-12">
      <v-fade-transition mode="out-in">
        <router-view />
      </v-fade-transition>
    </v-content>
      <v-footer width="100%" padless>
         <v-card
          flat
          tile
          width="100%"
          class="black text-center"
        >
        <v-card-text class="white--text">
          Released under the <a href="" target="_blank" rel="noopener" style="color:white;"><strong>... License</strong></a><br>
             Copyright &copy;  {{ new Date().getFullYear() }} — <strong>movie recommender</strong>
          </v-card-text>
         </v-card>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
    colors: [
        'indigo',
        'warning',
        'pink darken-2',
        'red lighten-1',
        'deep-purple accent-4',
      ],
      slides: [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth',
      ],
  }),
};
</script>
