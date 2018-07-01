<template>
  <div class="test">
    <el-row display="margin-top:10px">
      <el-input v-model="input" placeholder="请输入资源名" style="display: inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="add_compute_resource()" sytle="float:left; margin: 2px">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="resourceList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template scope="scope">{{ scope.row.pk }} </template>
        </el-table-column>

        <el-table-column prop="resource" label="资源" min-width="100">
          <template scope="scope">{{ scope.row.fields.name }}</template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>
<script>

export default{
  name: 'test',
  data () {
    return {
      input: '',
      resourceList: []
    }
  },
  mounted: function () {
    this.showList()
  },
  methods: {
    add_computer_resource () {
      this.$http.get('http://127.0.01:8000/api/add_computer_resource?name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showList()
          } else {
            this.$message.error('新增失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showList () {
      this.$http.get('http://127.0.0.1:8000/api/show_list')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.resList = res['list']
          } else {
            this.$message.error('查询失败')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
