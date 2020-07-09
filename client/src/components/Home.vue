<template>
  <v-container fluid class="px-12">
    <v-row class="mt-12">
      <div class="text-h5 text-md-h4">Popular</div>
    </v-row>

    <v-row class="mt-4" justify="space-between">
      <v-col
        v-for="movie in movies"
        :key="movie.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card>
          <v-img :src="movie.poster" contain max-height="390"> </v-img>
          <v-card-title>{{ movie.title}}</v-card-title>
          <div class="ml-3">
            <v-chip v-for="genre in movie.genres" :key="genre.id" class="mx-1" small>{{genre.name}}</v-chip>
          </div>
          <v-card-subtitle class="pt-3 pb-0">
            <v-icon color="primary">star</v-icon>
            <span>
              {{ movie.score.toFixed(1) }}
            </span>
          </v-card-subtitle>
          <v-card-text class="text--primary"> </v-card-text>

          <v-card-actions> </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",
  mounted(){
    this.getPopularMovies().then(data => {this.movies= data});
  },
  data: () => ({
    movies: []
  }),

  methods:{
    async getPopularMovies(){
      let response = await fetch('http://localhost:5000/api/movies/popular');
      let data = await response.json();
      data.forEach(movie => {
        fetch(`http://www.omdbapi.com/?i=${movie.imdb_id}&apikey=d3361710`)
        .then(response => {
          return response.json();
        })
        .then(json => { this.$set(movie,'poster',json.Poster) })
      });
      console.log("MOVIES", data)
      return data;
    },
  }
};
</script>
