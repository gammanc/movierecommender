<template>
  <v-container fluid class="px-12">
    <v-row class="mt-12">
      <div class="text-h5 text-md-h4">Populares</div>
    </v-row>

    <v-row class="mt-4" justify="space-between">
      <v-col
        v-for="movie in movies"
        :key="movie.id"
        cols="12"
        sm="6"
        md="4"
        lg="2"
      >
        <v-card>
          <v-img :src="movie.poster" contain max-height="390"> </v-img>
          <v-card-title>{{ movie.name }}</v-card-title>
          <v-card-subtitle class="pt-3 pb-0">
            <v-icon color="primary">star</v-icon>
            <span>
              {{ movie.rating.toFixed(1) }}
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

  data: () => ({
    movies: [
      {
        id: 1,
        name: "Interstellar",
        poster:
          "https://images-na.ssl-images-amazon.com/images/I/716P1xCmnPL._AC_SY879_.jpg",
        rating: 8.3,
      },
      {
        id: 2,
        name: "Deadpool",
        poster:
          "https://images-na.ssl-images-amazon.com/images/I/51Gh9OaWVcL._AC_.jpg",
        rating: 8.1,
      },
      {
        id: 3,
        name: "Guardians of the Galaxy",
        poster:
          "https://images-na.ssl-images-amazon.com/images/I/51T5sJngQLL._AC_.jpg",
        rating: 8.1,
      },
      {
        id: 4,
        name: "Mad Max: Fury Road",
        poster:
          "https://images-na.ssl-images-amazon.com/images/I/A1Y9Cqo1FmL._AC_SL1500_.jpg",
        rating: 8.4,
      },
      {
        id: 5,
        name: "Jurassic World",
        poster:
          "https://1.bp.blogspot.com/-lBYbuJgkQDw/Vi-zdMWzdBI/AAAAAAAARfo/IPl_TE8-p08/s1600/2.jpg",
        rating: 8.0,
      },
    ],
  }),
};
</script>
