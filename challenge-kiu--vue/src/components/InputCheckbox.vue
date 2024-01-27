<template>
  <div>
    <label for="dynamic-size">{{ label }}</label>
    <input v-model="localValue" type="checkbox" id="dynamic-size">
  </div>
</template>

<script>
export default {
  props: {
    label: { type: String, required: true },
    value: { type: Boolean, required: true },
  },
  computed: {
    localValue: {
      get() { return this.value; },
      set(value) { this.$emit('input', value); },
    },
  },
};
</script>