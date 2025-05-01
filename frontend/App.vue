<template>
    <div class="hoge">
        {{ message }}
    </div>
</template>

<script>
export default {
    name: 'App',
    data() {
        return {
            message: 'Hello Vue!'
        }
    }
}
</script>

<style lang="scss">
    .hoge {
        color: red;
    }
</style>
