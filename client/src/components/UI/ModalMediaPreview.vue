<template>
  <div class="modal-backdrop" @click="$emit('close')"></div>
  <img v-if="media.isImage" class="modal image" :src="media.url" alt="photo view">
  <video v-else class="modal image" autoplay loop controls :src="media.url" />
</template>

<script>
export default {
  emits: ['close'],
  props: {
    media: Object
  }
}
</script>

<style lang="scss" scoped>
.modal {
  position: fixed;
  top: 60px;
  z-index: 1000;
  left: 50%;
  border-radius: 10px;
  transform: translateX(-50%);
  box-shadow: 2px 3px 10px rgba(0, 0, 0, 0.2);
}

.image {
  max-width: 1280px;
  max-height: 720px;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.35);
  z-index: 100;
}
</style>