<template>
  <div>
    <v-carousel cycle height="600" hide-delimiter-background :show-arrows="false" class="padTop">
      <v-responsive>
        <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src">
          <v-sheet height="100%" color="rgba(0,0,0,.3)">
            <div class="carousel-content">
              <h1>{{ item.title }}</h1>
              <p style="color:#EEEEEE;">{{item.description}}</p>
            </div>
          </v-sheet>
        </v-carousel-item>
      </v-responsive>
    </v-carousel>
    <v-container fluid class="px-12">
      <v-row justify="center">
        <v-col cols="12" md="6" lg="4">
          <v-text-field
            placeholder="Search for a movie..."
            single-line
            filled
            rounded
            hide-details
            prepend-inner-icon="search"
            v-model="search_term"
            @blur="search_term = ''"
            :autocomplete="false"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row v-if="search_term">
        <v-col cols="12" md="6" lg="4" v-for="movie in filterMovies" :key="movie.id">
          <v-card>
            <v-card-text>
              <div class="d-flex align-center">
                <p class="text-body-1 text--primary">{{movie.title}}</p>
                <v-icon color="secondary" class="ml-auto">star</v-icon>
                <span style="color:#777;" class="subheading ml-2">{{movie.score.toFixed(2)}}</span>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <v-row v-if="!search_term">
        <div class="text-h5 text-md-h4 padTop px-12">Popular</div>
      </v-row>

      <v-row class="mt-4 px-10" justify="space-between" v-if="!search_term">
        <v-col v-for="movie in popular_movies" :key="movie.id" cols="12" sm="6" md="4" lg="3">
          <v-card>
            <v-img :src="movie.poster" contain max-height="390"></v-img>
            <v-card-title>{{ movie.title}}</v-card-title>
            <div class="ml-3">
              <v-chip
                v-for="genre in movie.genres"
                :key="genre.id"
                class="mx-1"
                small
              >{{genre.name}}</v-chip>
            </div>
            <v-card-subtitle class="pt-3 pb-0 d-flex align-center">
              <v-icon color="primary">star</v-icon>
              <span class="ml-2">{{ movie.score.toFixed(1) }}</span>
            </v-card-subtitle>
            <v-card-text class="text--primary"></v-card-text>

            <v-card-actions></v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import carousel_movies from "./movies";
export default {
  name: "Home",
  async mounted() {
    await this.getPopularMovies().then(data => {
      this.popular_movies = data;
    });

    await this.getMoviesList().then(movielist => {
      console.log("DATA", movielist);
      this.movies_list = movielist;
    });

    for (let i = 0; i < 10; i++) {
      console.log(this.movies_list[i]);
    }
  },
  data: () => ({
    popular_movies: [],
    movies_list: [],
    items: carousel_movies,
    search_term: ""
  }),

  methods: {
    async getPopularMovies() {
      let response = await fetch("http://localhost:5000/api/movies/popular");
      let data = await response.json();
      // data.forEach(movie => {
      //   fetch(`http://www.omdbapi.com/?i=${movie.imdb_id}&apikey=d3361710`)
      //   .then(response => {
      //     return response.json();
      //   })
      //   .then(json => { this.$set(movie,'poster',json.Poster) })
      // });
      data.forEach(movie => {
        this.$set(
          movie,
          "poster",
          "https://i.etsystatic.com/15963200/r/il/b10de2/1833903984/il_570xN.1833903984_yjpb.jpg"
        );
      });
      console.log("MOVIES", data);
      return data;
    },

    async getMoviesList() {
      let response = await fetch("http://localhost:5000/api/movies/names");
      let data = await response.json();
      return data;
    },

    showMoviesMenu(e) {
      e.preventDefault();
      this.showMenu = false;
      this.menu_x = e.clientX;
      this.menu_y = e.clientY;
      this.$nextTick(() => {
        this.showMenu = true;
      });
    }
  },

  computed: {
    filterMovies: function() {
      if (!this.search_term) return [];
      else {
        return this.movies_list.filter(movie => {
          return (
            movie.title
              .toLowerCase()
              .indexOf(this.search_term.toLowerCase()) !== -1
          );
        });
      }
    }
  }
};
</script>
<style>
.padTop {
  padding-top: 34px;
}

.carousel-content {
  width: 50%;
  height: 25%;
  background-color: transparent;
  text-align: left;
  left: 5%;
  bottom: 50px;
  position: absolute;
  margin-bottom: 64px;
}
</style>
