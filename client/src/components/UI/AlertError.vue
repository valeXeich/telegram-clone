<template>
    <div class="error">
        <p>{{ error }}</p>
    </div>
</template>

<script>
export default {
    props: {
        error: String
    }  
}
</script>

<style lang="scss" scoped>
.error {
    background-color: #2c0b0e;
    color: #ea868f;
    width: calc(100% - 10px);
    margin: 10px 0 0 0;
    padding: 10px;
    border-radius: 8px;
}
</style>