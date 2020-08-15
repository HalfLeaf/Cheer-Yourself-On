<template>
 <div class="wrap">
  <div id="box">
   <div id="marquee">{{text}}</div>
   <div id="copy"></div>
  </div>
  <div id="node">{{text}}</div>
 </div>
</template>
<script>
export default {
 name: 'marquee',
 props: ['lists'], // 父组件传入数据， 数组形式 [ "连雨不知春去"，"一晴方觉夏深"]
 data () {
  return {
   text: '' // 数组文字转化后的字符串
  }
 },
 methods: {
  move () {
  // 获取文字text 的计算后宽度 （由于overflow的存在，直接获取不到，需要独立的node计算）
   let width = document.getElementById('node').getBoundingClientRect().width
   let box = document.getElementById('box')
   let copy = document.getElementById('copy')
   copy.innertext = this.text // 文字副本填充
   let distance = 0 // 位移距离
   //设置位移
   setInterval(function () {
    distance = distance - 1
   // 如果位移超过文字宽度，则回到起点
    if (-distance >= width) {
     distance = 16
    }
    box.style.transform = 'translatex(' + distance + 'px)'
   }, 20)
  }
 },
// 把父组件传入的arr转化成字符串
 mounted: function () {
  for (let i = 0; i < this.lists.length; i++) {
   this.text += ' ' + this.lists[i] + "\n"
  }
 },
// 更新的时候运动
 updated: function () {
  this.move()
 }
}
</script>
<style lang="stylus" scoped>
.wrap
 overflow hidden

#box
 width 80000%

#box div
 float left

#marquee
  margin 0 16px 0 0

#node
 position absolute
 z-index -999
 top -999999px

</style>