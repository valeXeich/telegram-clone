<template>
    <div class="container">
        <input placeholder="Search" type="text" class="search">
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style lang="scss" scoped>

.container {
    max-width: 391px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    padding: 12.5px 0;
}

.search {
    background: rgba(255, 255, 255, 0.0605);
    border-radius: 3px;
    width: 100%;
    border: none;
    padding: 7px;
    color: #fff;
    border-bottom: 1px solid #97999C;
    &::placeholder {
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: rgba(255, 255, 255, 0.786);
        font-family: 'Segoe UI Variable'
    }
}
</style>