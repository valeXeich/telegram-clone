<template>
  <div>
    <img class="modal modal-image" v-if="isImage" :src="previewFile.url" alt="image" />
    <video class="modal modal-video" v-else-if="isVideo" autoplay loop :src="previewFile.url" />
    <div v-else class="modal modal-file">
      <div class="file-icon">
        <i class="bi bi-file-earmark-fill"></i>
      </div>
      <div class="file-info">
        <p class="file-name">{{ previewFile.name }}</p>
        <p class="file-size">{{ previewFile.size }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    previewFile: {
      type: Object,
      required: true,
    },
  },
  computed: {
    isImage() {
      return this.previewFile.type.includes("image");
    },
    isVideo() {
      return this.previewFile.type.includes("video");
    },
  },
};
</script>

<style lang="scss" scoped>
.modal {
  margin: 5px 0;
}

.modal-image {
  width: 100%;
  border-radius: 5px;
}

.modal-video {
  border-radius: 10px;
}

.modal-file {
  display: flex;
  align-items: center;
  gap: 5px;
  margin: 5px 0;

  .file-icon {
    font-size: 26px;
    background-color: #007dd2;
    padding: 10px;
    border-radius: 50%;
  }

  .file-info {
    .file-name {
      font-size: 18px;
      line-height: 1.5rem;
    }

    .file-size {
      font-size: 14px;
      color: #aaaa;
      line-height: 1rem;
    }
  }
}</style>
