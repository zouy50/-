var data = {
    name: "学生",
    children: [
        {name: "最近学习分析",
         children: [
             {name: "听讲专注",
              children: [{name: "提高",
                            children: [
                                {name: "表扬孩子最近表现"},
                                {name: "分析课频, 如果低建议加课频"}
                            ],
                            },
                           {name: "降低",
                            children: [
                                {name: "提升专注度的方法"},
                                {name: "最近课程难度是否偏难"},
                                {name: "老师是否需要换"}
                            ]}
                           ]
              },
             {name: "口语表达",
              children: [
                  {name: "提高",
                   children: [
                       {name: "表扬孩子口语表达提高"},
                       {name: "是否喜欢这个老师,推荐课"},
                   ],
                   },
                  {name: "降低",
                   children: [
                       {name: "年龄级别是否适合自然拼读",
                        children: [
                            {name: "适合",
                             children: [
                                 {name: "推荐自然拼读"}
                             ]},
                            {name: "不适合",
                             children: [
                                 {name: "转到上过自然拼读的"},
                             ]}
                        ]},
                       {name: "上过自然拼读",
                        children: [
                            {name: "UA成绩",
                             children: [
                                 {name: "没问题", children: [
                                     {name: "推荐聊一聊"},
                                 ]},
                                 {name: "低分或降低", children: [
                                     {name: "转到低分UA"},
                                 ]},
                             ]},
                        ]},
                       {name: "UA分数", children: [
                           {name: "提高", children: [

                           ]},
                           {name: "降低或一直很低", children: [
                               {name: "查看最近失分项或近期最多失分项", children: [
                                   {name: "对失分项进行查找资料反馈沟通"},
                               ]},
                               {name: "最近课频或者时间是否过于不稳定", children: [
                                   {name: "如果是就建议家长稳定课频，或者提高课频"}
                               ]}
                           ]},
                       ]},
                       {name: "老师是否稳定喜不喜欢"}
                   ]}
              ]},
             {name: "上课活跃",
              children: [
                  {name: "提高",
                   children: [
                       {name: "表扬"},
                       {name: "这个老师学生是否收藏并且好约", children: [
                               {name: "没有收藏并且好约", "value": "提醒收藏"},
                               {name: "没有收藏不好约", "value": "给家长收藏，并会尽力找很好的老师"},
                           ]},
                   ]},
                  {name: "降低",
                   children: [
                       {name: "教师是否稳定", children: [
                               {name: "不稳定", children: [
                                       {name: "建议设置专属外教"},
                                   ]},
                               {name: "稳定", children: [
                                       {name: "是否需要尝试换其他老师"}
                                   ]}
                           ]},
                       {name: "课程难度问题", children: [
                               {name: "", value: "lala"}
                           ], value: "lala"},
                   ]},
              ]},
             {name: "UA分数",
              children: [
                  {name: "降低",
                   children: [
                       {name: ""},
                   ]},
                  {name: "提高",
                   children: [
                       {name: ""},
                   ]}
              ]},
             {name: "作业完成度",
              children: [
                  {name: "降低",
                   children: [
                       {name: ""}
                   ]},
              ]},
             {name: "作业错题率",
              children: [
                  {name: "降低",
                   children: [

                   ]},
              ]},
             {name: ".其它.."},
         ]},
        {name: "课消分析"},
        {name: "节点问题"},
        {name: "最近联系天数分析"},
    ]
};



var lp_data = {
    name: LP,
    children: [
        {name: "必要工作", children: [

            ]}
    ]
}
