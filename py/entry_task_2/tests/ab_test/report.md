# activity_tab数据量100W，类别数量1K。



## 测试命令：
`ab -n 10000 -c 10 http://127.0.0.1:8000/entry_task/api/activity/list/\?min_datetime\=1588247287\&channel\=channel_10\&count\=2`
## 结果
```
Concurrency Level:      10
Time taken for tests:   10.644 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      12880000 bytes
HTML transferred:       11020000 bytes
Requests per second:    939.46 [#/sec] (mean)
Time per request:       10.644 [ms] (mean)
Time per request:       1.064 [ms] (mean, across all concurrent requests)
Transfer rate:          1181.67 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.7      1      15
Processing:     6   10   1.5      9      22
Waiting:        6    9   1.2      8      21
Total:          7   10   1.9     10      26

Percentage of the requests served within a certain time (ms)
  50%     10
  66%     11
  75%     11
  80%     12
  90%     13
  95%     14
  98%     15
  99%     17
 100%     26 (longest request)
```
## 测试命令：
`ab -n 10000 -c 50 http://127.0.0.1:8000/entry_task/api/activity/list/\?min_datetime\=1588247287\&channel\=channel_10\&count\=2`
## 结果
```
Concurrency Level:      50
Time taken for tests:   8.655 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      12880000 bytes
HTML transferred:       11020000 bytes
Requests per second:    1155.46 [#/sec] (mean)
Time per request:       43.273 [ms] (mean)
Time per request:       0.865 [ms] (mean, across all concurrent requests)
Transfer rate:          1453.35 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   1.8      1      53
Processing:     8   42   7.5     40      98
Waiting:        7   41   7.2     39      95
Total:          9   43   7.5     41     100

Percentage of the requests served within a certain time (ms)
  50%     41
  66%     43
  75%     45
  80%     47
  90%     52
  95%     56
  98%     63
  99%     70
 100%    100 (longest request)
```
## 测试命令：
`ab -n 10000 -c 100 http://127.0.0.1:8000/entry_task/api/activity/list/\?min_datetime\=1588247287\&channel\=channel_10\&count\=2`
## 结果
```
Concurrency Level:      100
Time taken for tests:   8.743 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      12880000 bytes
HTML transferred:       11020000 bytes
Requests per second:    1143.77 [#/sec] (mean)
Time per request:       87.430 [ms] (mean)
Time per request:       0.874 [ms] (mean, across all concurrent requests)
Transfer rate:          1438.65 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   3.5      1      75
Processing:    10   85  13.7     85     142
Waiting:        6   84  13.4     84     142
Total:         10   87  12.2     87     142

Percentage of the requests served within a certain time (ms)
  50%     87
  66%     90
  75%     92
  80%     94
  90%     99
  95%    107
  98%    117
  99%    123
 100%    142 (longest request)
```
## 测试命令：
`ab -n 10000 -c 200 http://127.0.0.1:8000/entry_task/api/activity/list/\?min_datetime\=1588247287\&channel\=channel_10\&count\=2`
## 结果
```
Concurrency Level:      200
Time taken for tests:   8.345 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      12880000 bytes
HTML transferred:       11020000 bytes
Requests per second:    1198.38 [#/sec] (mean)
Time per request:       166.892 [ms] (mean)
Time per request:       0.834 [ms] (mean, across all concurrent requests)
Transfer rate:          1507.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   4.2      1      76
Processing:    11  163  21.0    165     231
Waiting:        7  162  20.6    164     231
Total:         14  165  19.0    167     234

Percentage of the requests served within a certain time (ms)
  50%    167
  66%    170
  75%    172
  80%    173
  90%    182
  95%    190
  98%    205
  99%    216
 100%    234 (longest request)
```