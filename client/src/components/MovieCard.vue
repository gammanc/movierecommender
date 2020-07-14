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