<template>
  <div>
    <strong>服务器时间：<span v-html="serverTime"></span></strong>
    <div class="task-new">
      <el-button @click="dialogFormVisible = true" type="info">新增</el-button>
    </div>
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column type="index" label="序号" width="80"></el-table-column>
      <el-table-column property="0" label="ID" width="80"></el-table-column>
      <el-table-column property="1" label="任务名称" width="110"></el-table-column>
      <el-table-column property="2" label="结果">
        <template scope="scope">
          <div v-for="it in parse(scope.row[2])">{{it.touzhuresult}} 投注金额：{{it.bid_price_list}} 最高投注金额：{{it.top_price}} </div>
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
      <el-table-column property="8" label="周期" width="110">
        <template scope="scope">
          <div>{{scope.row[8]}}:{{scope.row[9]}}:{{scope.row[10]}}</div>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="230">
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
        <el-form-item v-for="(domain, index) in form.ids" :label="'商品ID-' + index" :key="domain.key" :prop="'ids.' + index + '.value'" :rules="{
                        required: true, message: '商品ID', trigger: 'blur'
                      }">
          <el-col :span="15">
            <el-input v-model="domain.value"></el-input>
          </el-col>
          <el-col :span="1"></el-col>
          <el-button @click.prevent="removeDomain(domain)">删除</el-button>
        </el-form-item>
        <el-form-item prop="loop_time" label="每天执行时间">
          <el-time-picker v-model="form.loop_time" placeholder="每天执行时间">
          </el-time-picker>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addDomain">新增ID</el-button>
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>

var host = '/api'
export default {
  data() {
    return {
      serverTime: '',
      dialogFormVisible: false,
      tableData: [],
      form: {
        loop_time: new Date(), ids: [{
          value: ''
        }]
      }
    }
  },
  created() {
    this.loadAll()
    setInterval(() => {
      var now = new Date();
      this.tableData.forEach((it) => {
        if (it[8] == now.getHours() && it[9] == now.getMinutes() && it[10] == now.getSeconds()) {
          this.loadAll();
        }
      })
    }, 900)
    setInterval(() => {
      this.$http.get(host + '/time').then((res) => {
        this.serverTime = res.body;
      })
    }, 1000)

  },
  methods: {

    parse(it) {
      try {
        return JSON.parse(it)
      }
      catch (e) {
      }

    },
    loadAll() {
      this.$http.get(host + '/list').then((res) => {
        this.tableData = res.body;
      })
    },
    removeDomain(item) {
      var index = this.form.ids.indexOf(item)
      if (index !== -1) {
        this.form.ids.splice(index, 1)
      }
    },
    addDomain() {
      this.form.ids.push({
        value: '',
        key: Date.now()
      });
    },
    save() {
      var form = this.form;

      this.$refs['form'].validate((valid) => {
        if (valid) {
          var h = form.loop_time.getHours();
          var m = form.loop_time.getMinutes();
          var s = form.loop_time.getSeconds();

          form.gn_id_list = form.ids.map((it) => {
            return it.value
          }).join(',')
          this.$http.get(host + '/add/' + `${encodeURIComponent(form.name)}/${encodeURIComponent(form.key)}/${encodeURIComponent(form.gn_id_list)}/${h}/${m}/${s}`).then((res) => {
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
