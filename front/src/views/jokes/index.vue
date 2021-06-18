<template>
  <div class="container">
    <el-table :data="[]" style="width: 100%" class="mt-2">
      <el-table-column prop="date" label="日期" width="180"> </el-table-column>
      <el-table-column prop="name" label="姓名" width="180"> </el-table-column>
      <el-table-column prop="address" label="地址"> </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator'

@Component({
  name: 'Jokes',
  components: {}
})
export default class extends Vue {}
</script>

<style lang="scss">
.container {
  padding: 20px;
}
</style>
