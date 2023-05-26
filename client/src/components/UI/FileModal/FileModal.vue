<template>
  <div class="modal-backdrop"></div>
  <div class="modal">
    <div class="modal-header">
      <h3>{{ title }}</h3>
      <div class="modal-close">
        <i class="bi bi-x" @click="$emit('close')"></i>
      </div>
    </div>
    <div class="modal-content">
      <FilePreview :previewFile="previewFile" />
      <FileCaption v-model="caption" :previewFile="previewFile" @addCaption="addMessage" />
    </div>
  </div>
</template>

<script>
import FilePreview from "./FilePreview.vue";
import FileCaption from "./FileCaption.vue";

export default {
  emits: ["close", "addMessage"],
  components: {
    FilePreview,
    FileCaption,
  },
  props: {
    title: String,
    previewFile: Object,
    createMessage: Function
  },
  data() {
    return {
      caption: "",
    };
  },
  methods: {
    addMessage() {
      const fileText = {
        image: "Picture",
        video: "Video",
        application: "Document",
        text: "Document"
      };
      const fileType = fileText[this.previewFile.type.split("/")[0]];
      const reader = new FileReader();
      reader.onload = () => {
        const encodedData = btoa(
          new Uint8Array(reader.result).reduce(
            (data, byte) => data + String.fromCharCode(byte),
            ""
          )
        );
        const message = this.createMessage(this.caption, true, fileType, encodedData)
        this.$emit("addMessage", 'send', message);
        this.caption = ''
      };

      reader.readAsArrayBuffer(this.previewFile.file);
    },
  },
};
</script>

<style lang="scss" scoped>
.modal {
  position: fixed;
  top: 60px;
  width: 420px;
  padding: 5px;
  background: rgb(33, 33, 33);
  z-index: 1000;
  left: 50%;
  border-radius: 10px;
  transform: translateX(-50%);
  box-shadow: 2px 3px 10px rgba(0, 0, 0, 0.2);
  color: #fff;

  .modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 404px;
    margin: 0 auto;
    font-size: 1.25rem;

    .modal-close {
      cursor: pointer;
      color: rgb(170, 170, 170);
      font-size: 26px;
      border-radius: 50%;
      padding: 7px;

      &:hover {
        background-color: rgba(170, 170, 170, 0.08);
        transition: background-color 0.15s, color 0.15s;
      }
    }
  }

  .modal-content {
    max-width: 404px;
    margin: 0 auto;
  }
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
