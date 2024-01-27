<template>
  <div class="container">
    <GenresSelector v-model="selectedGenres" />
    <InputCheckbox v-model="dynamicSize" label="Tamaño dinámico" />
    <ShowCard
      v-for="(show, showIndex) in displayedShows"
      :key="showIndex"
      :show="show"
      :dynamicSize="dynamicSize"
    />
  </div>
</template>

<script>
// components
import GenresSelector from '@/components/GenresSelector.vue';
import InputCheckbox from '@/components/InputCheckbox.vue';
import ShowCard from '@/components/ShowCard.vue';
// services
import { getShowsByPage } from "@/services/ShowsService.js";
// models
import { Show } from '@/models/Show.model.js';

export default {
  name: "ShowList",
  components: {
    GenresSelector,
    InputCheckbox,
    ShowCard,
},
  data() {
    return {
      dynamicSize: true,
      allShows: [],
      selectedGenres: [],
    };
  },
  computed: {
    displayedShows() {
      if (!this.selectedGenres.length) return this.allShows;
      return this.allShows.filter((show) => {
        return this.selectedGenres.every(genre => show.genres.includes(genre))
      });
    },
  },
  mounted() {
    this.setShowsData();
  },
  methods: {
    async setShowsData() {
      let shows = await getShowsByPage(1);
      console.log('shows', shows);
      shows = shows.map((show) => new Show(show));
      this.allShows = Show.sort(shows);
    },
  },
};
</script>

<style lang="css" scoped>
.container {
  background-color: lightgray;
  display: flex;
  gap: 1rem;
  flex-direction: column;
  padding-top: 1rem;
}
</style>
