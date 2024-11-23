# tx-java-app

安装所有应用
helm install  tx1  ./charts/nacos-config -n manager-test && 
helm install  tx2  ./charts/gateway -n manager-test && 
helm install  tx3  ./charts/eesu -n manager-test && 
helm install  tx4  ./charts/aesu -n manager-test && 
helm install  tx5  ./charts/dmsu -n manager-test && 
helm install  tx6  ./charts/statistic -n manager-test && 
helm install  tx7  ./charts/auth -n manager-test && 
helm install  tx8  ./charts/push -n manager-test

卸载所有应用
 helm uninstall  tx1 -n manager-test && 
 helm uninstall  tx2 -n manager-test && 
 helm uninstall  tx3 -n manager-test && 
 helm uninstall  tx4 -n manager-test && 
 helm uninstall  tx5 -n manager-test && 
 helm uninstall  tx6 -n manager-test && 
 helm uninstall  tx7 -n manager-test && 
 helm uninstall  tx8 -n manager-test




