<template>
  <vue-typed-js :strings="items | cookTyped":loopCount="32">
    <h1 class="typing"></h1>
  </vue-typed-js>
</template>

<script>
export default {
  props:{
    items:{
      type:Object,
      default: () => { title:"一诗 · 一词 · 一画 · 一茗 · 一成长"}
    }
  },
  filters: {
    cookTyped(item){
      return [item.title, item.author, ...item.content]
    }
  },
}
</script>
