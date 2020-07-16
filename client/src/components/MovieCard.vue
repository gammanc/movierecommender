<!--
  This file is part of movie recommender.

  Copyright (C) 2020 by Emerson Nolasco
  
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
  <v-card>
    <v-img :src="movie.poster" contain max-height="390"></v-img>
    <v-card-title>{{ movie.title}}</v-card-title>
    <div class="ml-3">
      <v-chip v-for="genre in movie.genres" :key="genre.id" class="mx-1" small>{{genre.name}}</v-chip>
    </div>
    <v-card-subtitle class="pt-3 pb-0 d-flex align-center">
      <v-icon color="primary">star</v-icon>
      <span class="ml-2">{{ movie.score.toFixed(1) }}</span>
    </v-card-subtitle>
    <v-card-text class="text--primary"></v-card-text>

    <v-card-actions></v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object
  }
};
</script>