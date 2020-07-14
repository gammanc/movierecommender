<template>
  <div>
     <v-carousel
      cycle
      height="600px"
      hide-delimiter-background
      :show-arrows="false"
      class="padTop"
    >
    <v-responsive>
        <v-carousel-item
           v-for="(item,i) in items"
              :key="i"
              :src="item.src"
        >
        <v-sheet height="100%" color="rgba(0,0,0,.3)">
          
              <div class=" carousel-content">
                <h1>{{ item.title }}</h1>
                 <p style="color:#EEEEEE;">{{item.description}}</p>
                </div>
              </v-sheet>
        </v-carousel-item>
    </v-responsive>
   </v-carousel>
    <v-container fluid class="px-12">
    <v-row>
      <div class="text-h5 text-md-h4 padTop px-12">Popular</div>
    </v-row>

    <v-row class="mt-4 px-10" justify="space-between">
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
  </div>
</template>

<script>
export default {
  name: "Home",
  mounted(){
    this.getPopularMovies().then(data => {this.movies= data});
  },
  data: () => ({
    movies: [],
      items: [
        {
          src: 'https://images.hdqwalls.com/wallpapers/bthumb/5k-top-gun-maverick-2020-ga.jpg', 
        description:'After more than thirty years of service as one of the Navy' +
        's top aviators , Pete Mitchell is where he belongs, pushing the envelope as a courageous'+
         'test pilot and dodging the advancement in rank that would ground him.',
         title:'Top Gun: Maverick (2020)',
        },
        {
          src: 'https://s.yimg.com/uu/api/res/1.2/pWtTfIAcUcZpBKyI7w1SKA--~B/aD02MzA7dz0xMjAwO3NtPTE7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/entertainment_weekly_785/b11ea3dd5d4ccae4c7f5f18d8838ce90',
         description:'Following the events at home, the Abbott family now face the terrors of the outside world. Forced to venture into the unknown,'+
         'they realize the creatures that hunt by sound are not the only threats lurking beyond the sand path.',
         title:'A Quiet Place part II (2020)',
        },
        {
          src: 'https://cdn.flickeringmyth.com/wp-content/uploads/2020/06/Ghosts-of-War-11.jpg',
          description:'Follows five battle-hardened American soldiers assigned to hold a French Chateau near the end of World War II. Formerly occupied by the Nazi high command, this unexpected respite quickly'
          +'descends into madness when they encounter a supernatural enemy far more terrifying than anything seen on the battlefield.',
          title: 'Ghosts of War (2020)',
          },
        {
          src: 'http://www.liveforfilm.com/wp-content/uploads/2019/12/john-david-washington-in-the-2020-film-tenet.jpg',
          description:'Armed with only one word -- Tenet -- and fighting for the survival of the entire world, the Protagonist'+
           'journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.',
         title:'Tenet(2020)',
        },
      ],
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
<style>
.padTop{
  padding-top:34px;
}

.carousel-content {
  width: 50%;
  height:25%;
  background-color: transparent;
  text-align: left;
  left: 5%;
  bottom:50px;
  position: absolute;
  margin-bottom: 64px;
}
</style>
