<template>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
    
        <Form-item label="任务名称" prop="name">
    
            <Input v-model="formValidate.name" placeholder="任务名称"></Input>
    
        </Form-item>
    
        <Form-item label="任务Class" prop="mail">
    
            <Input v-model="formValidate.mail" placeholder="任务Class"></Input>
    
        </Form-item>
    
        <Form-item label="内容等级" prop="mail">
    
            <Input-number :max="10" :min="1" v-model="value1"></Input-number>
    
        </Form-item>
    
        <Form-item label="运行类型" prop="interest">
    
            <Radio-group v-model="formValidate.gender">
    
                <Radio label="male">立即</Radio>
    
                <Radio label="female">时间</Radio>
    
                <Radio label="female">重复</Radio>
    
            </Radio-group>
    
        </Form-item>
    
        <Form-item label="日期">
    
            <Date-picker type="datetime" :options="options1" placeholder="选择日期"></Date-picker>
    
        </Form-item>
    
        <Form-item label="Cron">
    
            <Input v-model="formValidate.mail" placeholder="Cron"></Input>
    
        </Form-item>

        <Form-item label="url">
                <Row :gutter="8">
                    <Col span="8"> <Input v-model="formValidate.mail" placeholder="url"></Input></Col>
                     <Col span="4"> http://xxxx-{page}</Col>
                    <Col span="7"> <Input v-model="formValidate.mail" placeholder="开始" style="width:40%"></Input> - <Input  style="width:40%" v-model="formValidate.mail" placeholder="结束"></Input></Col>
                    <Col span="4"> <Button type="primary">生成</Button></Col>
                </Row>
        </Form-item>
    
        <Form-item label="urls" prop="desc">
    
            <Table border :columns="urlcol" :data="url_items"></Table>
    
        </Form-item>
    
        <Form-item>
    
            <Button type="primary" @click="handleSubmit('formValidate')">提交</Button>
    
            <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>
    
        </Form-item>
    
    </Form>
</template>
<script>
    export default {
    
        data() {
    
            return {
    
                urlcol: [{
                        title: 'url',
                        key: 'url',
                    },
                    {
                        title: '状态',
                        key: 'status'
                    },
                    {
                        title: '抓取时间',
                        key: 'address'
                    },
                    {
                        title: '操作',
                        key: 'action',
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.show(params.index)
                                        }
                                    }
    
                                }, '编辑'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                            this.remove(params.index)
                                        }
                                    }
                                }, '删除')
                            ]);
                        }
                    }
                ],
    
                url_items: [{
                        name: '王小明',
                        age: 18,
                        address: '北京市朝阳区芍药居'
                    },
                    {
                        name: '张小刚',
                        age: 25,
                        address: '北京市海淀区西二旗'
                    },
                    {
                        name: '李小红',
                        age: 30,
                        address: '上海市浦东新区世纪大道'
                    },
                    {
                        name: '周小伟',
                        age: 26,
                        address: '深圳市南山区深南大道'
                    }
                ],
            options1: {
                    shortcuts: [{
                            text: '今天',
                            value() {
                                return new Date();
                            }
                        },
                        {
                            text: '明天',
                            value() {
                                const date = new Date();
                                date.setTime(date.getTime() + 3600 * 1000 * 24);
                                return date;
                            }
                        },
                        {
                            text: '一周后',
                            value() {
                                const date = new Date();
                                date.setTime(date.getTime() + 3600 * 1000 * 24 * 7);
                                return date;
                            }
                        }
                    ]
                },
                formValidate: {
                    name: '',
                    mail: '',
                    city: '',
                    gender: '',
                    interest: [],
                    date: '',
                    time: '',
                    desc: ''
                },
                ruleValidate: {
                    name: [{
                        required: true,
                        message: '姓名不能为空',
                        trigger: 'blur'
                    }],
                    mail: [{
                            required: true,
                            message: '邮箱不能为空',
                            trigger: 'blur'
                        },
                        {
                            type: 'email',
                            message: '邮箱格式不正确',
                            trigger: 'blur'
                        }
                    ],
    
                    city: [{
                        required: true,
                        message: '请选择城市',
                        trigger: 'change'
                    }],
    
                    gender: [{
                        required: true,
                        message: '请选择性别',
                        trigger: 'change'
                    }],
    
                    interest: [{
    
                            required: true,
    
                            type: 'array',
    
                            min: 1,
    
                            message: '至少选择一个爱好',
    
                            trigger: 'change'
    
                        },
    
                        {
    
                            type: 'array',
    
                            max: 2,
    
                            message: '最多选择两个爱好',
    
                            trigger: 'change'
    
                        }
    
                    ],
    
                    date: [{
    
                        required: true,
    
                        type: 'date',
    
                        message: '请选择日期',
    
                        trigger: 'change'
    
                    }],
    
                    time: [{
    
                        required: true,
    
                        type: 'date',
    
                        message: '请选择时间',
    
                        trigger: 'change'
    
                    }],
    
                    desc: [{
    
                            required: true,
    
                            message: '请输入个人介绍',
    
                            trigger: 'blur'
    
                        },
    
                        {
    
                            type: 'string',
    
                            min: 20,
    
                            message: '介绍不能少于20字',
    
                            trigger: 'blur'
    
                        }
    
                    ]
    
                }
    
        }
    
    },
    
    methods: {
    
        handleSubmit(name) {
    
            this.$refs[name].validate((valid) => {
    
                if (valid) {
    
                    this.$Message.success('提交成功!');
    
                } else {
    
                    this.$Message.error('表单验证失败!');
    
                }
    
            })
    
        },
    
        handleReset(name) {
    
            this.$refs[name].resetFields();
    
        }
    
    }
    
    }
</script>