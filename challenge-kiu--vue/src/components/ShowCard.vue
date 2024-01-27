<template>
  <div class="card" :class="{ 'dynamic-size': dynamicSize }">
    <div class="card__content">
      <img
        class="card__content--left-column"
        :src="show.image"
        alt="image"
      />
      <div class="card__content--right-column">
        <h1>{{ show.name }}</h1>
        <div class="card__content--right-column--type-and-newtwork">
          <p class="type">{{ show.type }}</p>
          <p>Network: {{ show.network }}</p>
        </div>
      </div>
    </div>
    <div class="card__buttons">
      <p>
        <a :href="show.officialSite">
          <button>Official Site</button>
        </a>
      </p>
    </div>
  </div>
</template>

<script>
// models
import { Show } from '@/models/Show.model.js'

export default {
  props: {
    show: { type: Show, required: true },
    dynamicSize: { type: Boolean, default: false },
  },
};
</script>

<style lang="css" scoped>
* {
  margin: 0;
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  min-width: 23.5rem;
  width: 23.5rem;
  max-width: 80%;
  margin: auto;
  text-align: center;
  font-family: arial;
  background-color: white;
}
.card.dynamic-size {
  width: 100%;
}
.card__content {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  gap: 1rem;
  padding-top: 1rem;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-bottom: 0.35rem;
}
.card.dynamic-size .card__content {
  justify-content: center;
}
.card__content--right-column {
  padding-top: 0.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  flex-grow: 1;
}
.card.dynamic-size .card__content .card__content--right-column {
  flex-grow: 0;
}
.card__content--right-column--type-and-newtwork {
  padding-top: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.type {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

img {
  width: 100px;
  height: auto;
  margin: auto 0;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover,
a:hover {
  opacity: 0.7;
}
</style>
