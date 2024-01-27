<template>
  <div>
    <label>Género</label>
    <select v-model="currentSelectedValue" @change="selectGenre()">
      <option :value="null">* Selecciona los géneros *</option>
      <option
        v-for="(genre, genreIndex) in displayedGenres"
        :key="genreIndex"
        :value="genre"
      >
        {{ genre }}
      </option>
    </select>
    <div v-if="selectedGenres.length" class="selecteds-container">
      <span>Seleccionados: </span>
      <div
        v-for="(genre, genreIndex) in selectedGenres"
        :key="genreIndex"
        @click="unselectGenre(genre)"
      >
        <div class="genre-item">
          {{ genre }}
          <div class="remove-genre-btn">x</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// services
import { getShows } from '@/services/ShowsService.js';

export default {
  name: 'GenreSelector',
  props: {
    value: { type: Array, required: true },
  },
  data() {
    return {
      allGenres: [],
      currentSelectedValue: null,
    };
  },
  computed: {
    displayedGenres() {
      return this.allGenres.filter((genre) => !this.selectedGenres.includes(genre));
    },
    selectedGenres: {
      get() { return this.value; },
      set(value) { this.$emit('input', value); },
    },
  },
  mounted() {
    this.getAllGenres();
  },
  methods: {
    async getAllGenres() {
      let genres = (await getShows()).map((show) => show.genres).flat();
      this.allGenres = [...new Set(genres)].sort();
    },
    selectGenre() {
      this.selectedGenres.push(this.currentSelectedValue);
      this.selectedGenres = this.selectedGenres.sort();
      this.currentSelectedValue = null;
    },
    unselectGenre(genre) {
      const index = this.selectedGenres.findIndex((g) => g === genre);
      this.selectedGenres.splice(index, 1);
    },
  },
};
</script>

<style lang="css" scoped>
.selecteds-container {
  border: 1px dashed #aaa;
  padding: 0.5rem;
  display: flex;
  flex-direction: column;
  width: 200px;
  margin: 0.25rem auto;
  gap: 0.5rem;
  border-radius: 0.5rem;
}
.genre-item {
  background-color: #aaa;
  color: white;
  border-radius: 2rem;
  text-align: left;
  padding: 0.25rem 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  transition: 0.15s;
}
.genre-item:hover {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.15);
}
.remove-genre-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-size: 0.85rem;
  opacity: 0;
  width: 1rem;
  height: 1rem;
  color: #ddd;
  background-color: #777;
  transition: 0.15s;
}
.genre-item:hover .remove-genre-btn {
  opacity: 1;
}
.remove-genre-btn:hover {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.25);
}
</style>
