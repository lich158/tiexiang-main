{{- define "tx-gateway.name" -}}
tx-gateway
{{- end }}

{{- define "tx-gateway.fullname" -}}
{{ .Release.Name }}-tx-gateway
{{- end }}

{{- define "tx-gateway.pvcName" -}}
{{ .Release.Name }}-gateway-log
{{- end }}
