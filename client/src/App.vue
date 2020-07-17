<!--
  This file is part of movie recommender.

  Copyright (C) 2020 by Emerson Nolasco and Karla Cruz
  
  movie recommender is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  movie recommender is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
 -->
<template>
  <v-app height="100%">
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

      <v-btn href="https://github.com/gammanc/movierecommender" target="_blank" icon>
        <v-icon>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content class="" style="padding-top:34px;">
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
          Content from
          <a href="http://www.omdbapi.com/" target="_blank" rel="noopener" style="color:white; text-decoration:none;"><strong>OMDb Api</strong></a> by 
          <a href="mailto:bfritz@fadingsignal.com" target="_blank" rel="noopener" style="color:white; text-decoration:none;"><strong>Brian Fritz</strong></a><br>
          licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank" rel="noopener" style="color:white; text-decoration:none;"><strong>CC BY-NC 4.0</strong></a><br>
          <br><v-divider></v-divider><br>
          Released under the <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank" rel="noopener" style="color:white; text-decoration:none;"><strong>GPLv3 License</strong></a><br>
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
      
  }),
};
</script>

