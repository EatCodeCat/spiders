<template>
  <div>
    <div class="task-new">
      <el-button @click="dialogFormVisible = true" type="info">新增</el-button>
    </div>
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column type="index" label="序号" width="80"></el-table-column>
      <el-table-column property="1" label="任务名称" width="110"></el-table-column>
      <el-table-column property="2" label="结果">
        <template scope="scope">
          <div v-for="it in parse(scope.row[2])">{{it}}</div>
        </template>
      </el-table-column>
      <el-table-column property="3" label="关键字" width="120"></el-table-column>
      <el-table-column property="4" label="商品ID列表"></el-table-column>
      <el-table-column property="5" label="状态" width="100">
        <template scope="scope">
          <el-tag :type="scope.row[5] == 0 ? 'success' : 'danger'">{{scope.row[5] == 0 ? '等待执行' :(scope.row[5] == 1?'暂停':'停止')}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column property="6" label="执行时间" width="150"></el-table-column>
      <el-table-column label="操作" width="150">
        <template scope="scope">
          <el-button size="small" @click="handleEdit(scope.$index, scope.row)">{{scope.row[5] == 0 ? '暂停' : '执行'}}</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="任务" :visible.sync="dialogFormVisible">
      <el-form :model="form" label-width="120px" ref="form">
        <el-form-item prop="name" label="任务名称" :rules="{
                  required: true, message: '任务名称不能为空', trigger: 'blur'}">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item prop="key" label="关键字" :rules="{
                  required: true, message: '关键字不能为空', trigger: 'blur'
                }">
          <el-input v-model="form.key"></el-input>
        </el-form-item>
        <el-form-item prop="gn_id_list" label="商品ID列表" :rules="{
                  required: true, message: '商品ID列表不能为空', trigger: 'blur'
                }">
          <el-input v-model="form.gn_id_list" placeholder="id列表用,隔开"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>

var host = '/api/'
export default {
  data() {
    return {
      dialogFormVisible: false,
      tableData: [],
      form: {}
    }
  },
  created() {
    this.loadAll()

  },
  methods: {
    parse(it){
      try{
        return JSON.parse(it)
      }
      catch(e){

      }
       
    },
    loadAll() {
      this.$http.get(host + '/list').then((res) => {
        this.tableData = res.body;
      })
    },
    save() {
      var form = this.form;

      this.$refs['form'].validate((valid) => {
        if (valid) {
          this.$http.get(host + '/add/' + encodeURIComponent(`${form.name}/${form.key}/${form.gn_id_list}`)).then((res) => {
            this.$message({
              showClose: true,
              message: '保存成功',
              type: 'success'
            });
            this.dialogFormVisible = false;
            this.loadAll()
          }, () => {
            this.$message({
              showClose: true,
              message: '出错了！！！！',
              type: 'error'
            });
          })
        } else {
          console.log('error submit!!');
          return false;
        }
      });

    },
    handleEdit(index, row) {
      var id = row[0]
      if (this.tableData[index][5] == 0) {

        this.$http.get(host + '/pause/' + row[0]).then((res) => {
          this.$set(this.tableData[index], 5, 1);
          this.$nextTick()
        }, () => {
          this.$message({
            showClose: true,
            message: '出错了！！！！',
            type: 'error'
          });
        })
      }
      else {

        this.$http.get(host + '/resume/' + row[0]).then((res) => {
          this.$set(this.tableData[index], 5, 0);
          this.$nextTick()
        }, () => {
          this.$message({
            showClose: true,
            message: '出错了！！！！',
            type: 'error'
          });
        })
      }

    },
    handleDelete(index, row) {
      this.$http.get(host + '/remove/' + row[0]).then((res) => {
        this.tableData.splice(index, 1)
      }, () => {
        this.$message({
          showClose: true,
          message: '出错了！！！！',
          type: 'error'
        });
      })
    }
  }
}
</script>
<style>
.task-new {
  float: right;
  margin: 20px;
}
</style>
