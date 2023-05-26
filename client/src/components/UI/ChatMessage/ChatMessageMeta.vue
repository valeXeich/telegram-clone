<template>
  <div :class="$attrs.class">
    <p>
      {{ created_at }}
      <i v-if="readed" class="bi bi-check-all"></i>
      <i v-else class="bi bi-check"></i>
    </p>
  </div>
</template>

<script>
export default {
  props: {
    created_at: String,
    readed: Boolean
  },
};
</script>

<style lang="scss" scoped>
p {
  font-size: 12px;
  color: $transparent-white;

  i {
    font-size: 13px;
    color: $white;
  }
}
</style>
