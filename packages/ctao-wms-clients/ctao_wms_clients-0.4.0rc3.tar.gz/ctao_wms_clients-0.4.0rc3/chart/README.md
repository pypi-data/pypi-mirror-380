# wms

![Version: 0.0.0-dev](https://img.shields.io/badge/Version-0.0.0--dev-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: dev](https://img.shields.io/badge/AppVersion-dev-informational?style=flat-square)

A Helm chart to deploy the Workload Management System of CTAO

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://diracgrid.github.io/diracx-charts | diracx | 1.0.0-alpha.2 |
| oci://harbor.cta-observatory.org/dpps | cert-generator-grid | v3.1.0 |
| oci://harbor.cta-observatory.org/dpps | cvmfs | v0.5.2 |
| oci://harbor.cta-observatory.org/dpps | iam(dpps-iam) | v0.1.0 |
| oci://harbor.cta-observatory.org/proxy_cache/bitnamicharts | mariadb | 20.5.5 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| cert-generator-grid | object | `{"enabled":true,"extra_server_names":["iam.test.example","voms.test.example","fts","dirac-server"],"generatePreHooks":true,"users":[{"name":"DPPS User","suffix":""},{"name":"DPPS User Unprivileged","suffix":"-unprivileged"},{"name":"Non-DPPS User","suffix":"-non-dpps"}]}` | Settings for the certificate generator |
| cvmfs | object | `{"enabled":true,"publish_docker_images":["harbor.cta-observatory.org/proxy_cache/library/python:3.12-slim"],"publisher":{"image":{"repository_prefix":"harbor.cta-observatory.org/proxy_cache/bitnamilegacy/kubectl","tag":"1.31.1"}}}` | Configuration for the cvmfs subchart, included for testing |
| dev | object | `{"client_image_tag":null,"mount_repo":true,"run_tests":true,"sleep":false}` | Settings for local development |
| dev.client_image_tag | string | `nil` | tag of the image used to run helm tests |
| dev.mount_repo | bool | `true` | mount the repo volume to test the code as it is being developed |
| dev.run_tests | bool | `true` | run tests in the container |
| dev.sleep | bool | `false` | sleep after test to allow interactive development |
| dirac_server | object | `{"podAnnotations":{},"podLabels":{},"podSecurityContext":{},"resetDatabase":true,"securityContext":{},"webApp":{"enabled":true}}` | Setting for the main DIRAC server pod |
| dirac_server.resetDatabase | bool | `true` | Recreates DIRAC database from scratch. Useful at first installation, but destructive on update: should be changed immediately after the first installation. |
| diracx.developer.enabled | bool | `true` |  |
| diracx.developer.localCSPath | string | `"/local_cs_store"` |  |
| diracx.developer.urls.diracx | string | `"http://wms-diracx:8000"` |  |
| diracx.developer.urls.iam | string | `"http://dpps-iam:8080"` |  |
| diracx.developer.urls.minio | string | `"http://wms-minio:32000"` |  |
| diracx.dex.enabled | bool | `false` |  |
| diracx.diracx.hostname | string | `"wms-diracx"` |  |
| diracx.diracx.osDbs.dbs.JobParametersDB | string | `nil` |  |
| diracx.diracx.settings.DIRACX_CONFIG_BACKEND_URL | string | `"git+file:///cs_store/initialRepo"` |  |
| diracx.diracx.settings.DIRACX_LEGACY_EXCHANGE_HASHED_API_KEY | string | `"19628aa0cb14b69f75b2164f7fda40215be289f6e903d1acf77b54caed61a720"` |  |
| diracx.diracx.settings.DIRACX_SANDBOX_STORE_AUTO_CREATE_BUCKET | string | `"true"` |  |
| diracx.diracx.settings.DIRACX_SANDBOX_STORE_BUCKET_NAME | string | `"sandboxes"` |  |
| diracx.diracx.settings.DIRACX_SANDBOX_STORE_S3_CLIENT_KWARGS | string | `"{\"endpoint_url\": \"http://wms-minio:9000\", \"aws_access_key_id\": \"rootuser\", \"aws_secret_access_key\": \"rootpass123\"}"` |  |
| diracx.diracx.settings.DIRACX_SERVICE_AUTH_ACCESS_TOKEN_EXPIRE_MINUTES | string | `"120"` |  |
| diracx.diracx.settings.DIRACX_SERVICE_AUTH_ALLOWED_REDIRECTS | string | `"[\"http://wms-diracx:8000/api/docs/oauth2-redirect\", \"http://wms-diracx:8000/#authentication-callback\"]"` |  |
| diracx.diracx.settings.DIRACX_SERVICE_AUTH_REFRESH_TOKEN_EXPIRE_MINUTES | string | `"360"` |  |
| diracx.diracx.settings.DIRACX_SERVICE_AUTH_TOKEN_ISSUER | string | `"http://wms-diracx:8000"` |  |
| diracx.diracx.settings.DIRACX_SERVICE_AUTH_TOKEN_KEYSTORE | string | `"file:///keystore/jwks.json"` |  |
| diracx.diracx.sqlDbs.dbs.AuthDB.internalName | string | `"DiracXAuthDB"` |  |
| diracx.diracx.sqlDbs.dbs.JobDB | string | `nil` |  |
| diracx.diracx.sqlDbs.dbs.JobLoggingDB | string | `nil` |  |
| diracx.diracx.sqlDbs.dbs.SandboxMetadataDB | string | `nil` |  |
| diracx.diracx.sqlDbs.dbs.TaskQueueDB | string | `nil` |  |
| diracx.diracx.sqlDbs.default.host | string | `"dirac-db:3306"` |  |
| diracx.diracx.sqlDbs.default.password | string | `"dirac-db"` |  |
| diracx.diracx.sqlDbs.default.rootPassword | string | `"dirac-db-root"` |  |
| diracx.diracx.sqlDbs.default.rootUser | string | `"root"` |  |
| diracx.diracx.sqlDbs.default.user | string | `"Dirac"` |  |
| diracx.diracx.startupProbe.failureThreshold | int | `60` |  |
| diracx.diracx.startupProbe.periodSeconds | int | `15` |  |
| diracx.diracx.startupProbe.timeoutSeconds | int | `5` |  |
| diracx.elasticsearch.enabled | bool | `false` |  |
| diracx.enabled | bool | `true` |  |
| diracx.global.activeDeadlineSeconds | int | `900` |  |
| diracx.global.batchJobTTL | int | `3600` |  |
| diracx.global.imagePullPolicy | string | `"Always"` |  |
| diracx.global.images.client | string | `"ghcr.io/diracgrid/diracx/client"` |  |
| diracx.global.images.services | string | `"ghcr.io/diracgrid/diracx/services"` |  |
| diracx.global.images.tag | string | `"v0.0.1a50"` |  |
| diracx.grafana.enabled | bool | `false` |  |
| diracx.indigoiam.enabled | bool | `false` |  |
| diracx.indigoiam.image.repository | string | `"indigoiam/iam-login-service"` |  |
| diracx.indigoiam.image.tag | string | `"v1.13.0-rc2"` |  |
| diracx.initSql.enabled | bool | `false` |  |
| diracx.initSql.env | object | `{}` |  |
| diracx.jaeger.enabled | bool | `false` |  |
| diracx.minio.environment.MINIO_BROWSER_REDIRECT_URL | string | `"http://wms-minio:32001/"` |  |
| diracx.minio.rootPassword | string | `"rootpass123"` |  |
| diracx.minio.rootUser | string | `"rootuser"` |  |
| diracx.mysql.enabled | bool | `false` |  |
| diracx.opensearch.enabled | bool | `true` |  |
| diracx.opentelemetry-collector.enabled | bool | `false` |  |
| diracx.prometheus.enabled | bool | `false` |  |
| diracx.rabbitmq.auth.existingErlangSecret | string | `"rabbitmq-secret"` |  |
| diracx.rabbitmq.auth.existingPasswordSecret | string | `"rabbitmq-secret"` |  |
| diracx.rabbitmq.containerSecurityContext.enabled | bool | `false` |  |
| diracx.rabbitmq.enabled | bool | `true` |  |
| diracx.rabbitmq.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| diracx.rabbitmq.image.repository | string | `"bitnamilegacy/rabbitmq"` |  |
| diracx.rabbitmq.podSecurityContext.enabled | bool | `false` |  |
| fullnameOverride | string | `""` |  |
| global.dockerRegistry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| global.images.busybox.repository | string | `"harbor.cta-observatory.org/proxy_cache/busybox"` |  |
| global.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| global.storageClassName | string | `"standard"` |  |
| iam.bootstrap.config.clients[0].client_id | string | `"dpps-test-client"` |  |
| iam.bootstrap.config.clients[0].client_name | string | `"WMS Test Client"` |  |
| iam.bootstrap.config.clients[0].client_secret | string | `"secret"` |  |
| iam.bootstrap.config.clients[0].grant_types[0] | string | `"authorization_code"` |  |
| iam.bootstrap.config.clients[0].grant_types[1] | string | `"password"` |  |
| iam.bootstrap.config.clients[0].grant_types[2] | string | `"client_credentials"` |  |
| iam.bootstrap.config.clients[0].grant_types[3] | string | `"urn:ietf:params:oauth:grant_type:redelegate"` |  |
| iam.bootstrap.config.clients[0].grant_types[4] | string | `"refresh_token"` |  |
| iam.bootstrap.config.clients[0].scopes[0] | string | `"scim:write"` |  |
| iam.bootstrap.config.clients[0].scopes[1] | string | `"scim:read"` |  |
| iam.bootstrap.config.clients[0].scopes[2] | string | `"offline_access"` |  |
| iam.bootstrap.config.clients[0].scopes[3] | string | `"openid"` |  |
| iam.bootstrap.config.clients[0].scopes[4] | string | `"profile"` |  |
| iam.bootstrap.config.clients[0].scopes[5] | string | `"iam:admin.write"` |  |
| iam.bootstrap.config.clients[0].scopes[6] | string | `"iam:admin.read"` |  |
| iam.bootstrap.config.issuer | string | `"http://wms-dpps-iam-login-service:8080"` |  |
| iam.bootstrap.config.users[0].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| iam.bootstrap.config.users[0].cert.env_var | string | `"X509_USER_CERT"` |  |
| iam.bootstrap.config.users[0].cert.kind | string | `"env_var_file"` |  |
| iam.bootstrap.config.users[0].email | string | `"dpps@test.example"` |  |
| iam.bootstrap.config.users[0].family_name | string | `"User"` |  |
| iam.bootstrap.config.users[0].given_name | string | `"DPPS"` |  |
| iam.bootstrap.config.users[0].groups[0] | string | `"ctao.dpps.test"` |  |
| iam.bootstrap.config.users[0].groups[1] | string | `"dpps_group"` |  |
| iam.bootstrap.config.users[0].groups[2] | string | `"dpps_genpilot"` |  |
| iam.bootstrap.config.users[0].groups[3] | string | `"dirac_admin"` |  |
| iam.bootstrap.config.users[0].groups[4] | string | `"dirac_user"` |  |
| iam.bootstrap.config.users[0].password | string | `"dpps-password"` |  |
| iam.bootstrap.config.users[0].role | string | `"ROLE_USER"` |  |
| iam.bootstrap.config.users[0].subject_dn | string | `"DPPS User"` |  |
| iam.bootstrap.config.users[0].username | string | `"dpps_user"` |  |
| iam.bootstrap.config.users[1].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| iam.bootstrap.config.users[1].cert.env_var | string | `"X509_USER_CERT"` |  |
| iam.bootstrap.config.users[1].cert.kind | string | `"env_var_file"` |  |
| iam.bootstrap.config.users[1].email | string | `"dpps@test.example"` |  |
| iam.bootstrap.config.users[1].family_name | string | `"User"` |  |
| iam.bootstrap.config.users[1].given_name | string | `"TestDpps"` |  |
| iam.bootstrap.config.users[1].groups[0] | string | `"ctao.dpps.test"` |  |
| iam.bootstrap.config.users[1].groups[1] | string | `"dpps_group"` |  |
| iam.bootstrap.config.users[1].groups[2] | string | `"dirac_user"` |  |
| iam.bootstrap.config.users[1].password | string | `"test-password"` |  |
| iam.bootstrap.config.users[1].role | string | `"ROLE_USER"` |  |
| iam.bootstrap.config.users[1].subject_dn | string | `"DPPS User"` |  |
| iam.bootstrap.config.users[1].username | string | `"test_user"` |  |
| iam.bootstrap.config.users[2].email | string | `"dpps@test.example"` |  |
| iam.bootstrap.config.users[2].family_name | string | `"User"` |  |
| iam.bootstrap.config.users[2].given_name | string | `"TestAdmin"` |  |
| iam.bootstrap.config.users[2].groups[0] | string | `"ctao.dpps.test"` |  |
| iam.bootstrap.config.users[2].password | string | `"test-password"` |  |
| iam.bootstrap.config.users[2].role | string | `"ROLE_ADMIN"` |  |
| iam.bootstrap.config.users[2].username | string | `"admin-user"` |  |
| iam.bootstrap.env[0].name | string | `"X509_NON_DPPS_USER_CERT"` |  |
| iam.bootstrap.env[0].value | string | `"/tmp/user-non-dpps-cert.pem"` |  |
| iam.bootstrap.env[1].name | string | `"X509_UNPRIVILEGED_DPPS_USER_CERT"` |  |
| iam.bootstrap.env[1].value | string | `"/tmp/user-unprivileged-cert.pem"` |  |
| iam.bootstrap.extraVolumeMounts[0].mountPath | string | `"/tmp/userkey.pem"` |  |
| iam.bootstrap.extraVolumeMounts[0].name | string | `"dppsuser-certkey-400"` |  |
| iam.bootstrap.extraVolumeMounts[0].subPath | string | `"dppsuser.key.pem"` |  |
| iam.bootstrap.extraVolumeMounts[1].mountPath | string | `"/tmp/usercert.pem"` |  |
| iam.bootstrap.extraVolumeMounts[1].name | string | `"dppsuser-certkey-600"` |  |
| iam.bootstrap.extraVolumeMounts[1].subPath | string | `"dppsuser.pem"` |  |
| iam.bootstrap.extraVolumes[0].name | string | `"dppsuser-certkey"` |  |
| iam.bootstrap.extraVolumes[0].secret.defaultMode | int | `272` |  |
| iam.bootstrap.extraVolumes[0].secret.secretName | string | `"wms-dppsuser-certkey"` |  |
| iam.bootstrap.extraVolumes[1].name | string | `"dppsuser-certkey-600"` |  |
| iam.bootstrap.extraVolumes[1].secret.defaultMode | int | `384` |  |
| iam.bootstrap.extraVolumes[1].secret.secretName | string | `"wms-dppsuser-certkey"` |  |
| iam.bootstrap.extraVolumes[2].name | string | `"dppsuser-certkey-400"` |  |
| iam.bootstrap.extraVolumes[2].secret.defaultMode | int | `256` |  |
| iam.bootstrap.extraVolumes[2].secret.secretName | string | `"wms-dppsuser-certkey"` |  |
| iam.bootstrap.image.pullPolicy | string | `"IfNotPresent"` |  |
| iam.bootstrap.image.repository | string | `"harbor.cta-observatory.org/dpps/dpps-iam-client"` |  |
| iam.bootstrap.image.tag | string | `nil` |  |
| iam.bootstrap.tag | string | `nil` |  |
| iam.cert-generator-grid.enabled | bool | `false` |  |
| iam.dev.mount_repo | bool | `false` |  |
| iam.enabled | bool | `true` |  |
| iam.iam.database.external.existingSecret | string | `""` |  |
| iam.iam.database.external.host | string | `"wms-mariadb"` |  |
| iam.iam.database.external.name | string | `"indigo-iam"` |  |
| iam.iam.database.external.password | string | `"PassW0rd"` |  |
| iam.iam.database.external.port | int | `3306` |  |
| iam.iam.database.external.username | string | `"indigo-iam"` |  |
| iam.iam.fullnameOverride | string | `"wms-dpps-iam"` |  |
| iam.iam.ingress.annotations."nginx.ingress.kubernetes.io/ssl-passthrough" | string | `"true"` |  |
| iam.iam.ingress.annotations."nginx.ingress.kubernetes.io/ssl-redirect" | string | `"true"` |  |
| iam.iam.ingress.className | string | `"nginx"` |  |
| iam.iam.ingress.enabled | bool | `true` |  |
| iam.iam.ingress.tls.enabled | bool | `true` |  |
| iam.iam.ingress.tls.secretName | string | `"wms-tls"` |  |
| iam.iam.loginService.config.java.opts | string | `"-Xms512m -Xmx512m -Djava.security.egd=file:/dev/./urandom -Dspring.profiles.active=prod -Dlogging.level.org.springframework.web=DEBUG -Dlogging.level.com.indigo=DEBUG"` |  |
| iam.iam.mariadb.enabled | bool | `false` |  |
| iam.iam.mysql.enabled | bool | `false` |  |
| iam.nameOverride | string | `"dpps-iam"` |  |
| iam.vomsAA.config.host | string | `"voms.test.example"` |  |
| iam.vomsAA.config.voName | string | `"ctao.dpps.test"` |  |
| iam.vomsAA.deployment.replicas | int | `1` |  |
| iam.vomsAA.enabled | bool | `true` |  |
| iam.vomsAA.ingress.className | string | `"nginx"` |  |
| iam.vomsAA.ingress.enabled | bool | `true` |  |
| iam.vomsAA.ingress.tls.enabled | bool | `true` |  |
| iam.vomsAA.lsc.entries[0] | string | `"/CN=voms.test.example"` |  |
| iam.vomsAA.lsc.entries[1] | string | `"/CN=DPPS Development CA"` |  |
| iam.vomsAA.nginxVoms.resources.limits.memory | string | `"256Mi"` |  |
| iam.vomsAA.nginxVoms.resources.requests.cpu | string | `"100m"` |  |
| iam.vomsAA.nginxVoms.resources.requests.memory | string | `"128Mi"` |  |
| iam.vomsAA.resources.limits.cpu | string | `"500m"` |  |
| iam.vomsAA.resources.limits.memory | string | `"1Gi"` |  |
| iam.vomsAA.resources.requests.cpu | string | `"200m"` |  |
| iam.vomsAA.resources.requests.memory | string | `"512Mi"` |  |
| iamConfig.clients[0].client_id | string | `"dpps-test-client"` |  |
| iamConfig.clients[0].client_name | string | `"WMS Test Client"` |  |
| iamConfig.clients[0].client_secret | string | `"secret"` |  |
| iamConfig.clients[0].grant_types[0] | string | `"authorization_code"` |  |
| iamConfig.clients[0].grant_types[1] | string | `"password"` |  |
| iamConfig.clients[0].grant_types[2] | string | `"client_credentials"` |  |
| iamConfig.clients[0].grant_types[3] | string | `"urn:ietf:params:oauth:grant_type:redelegate"` |  |
| iamConfig.clients[0].grant_types[4] | string | `"refresh_token"` |  |
| iamConfig.clients[0].redirect_uris[0] | string | `"http://wms-diracx:8000/api/auth/device/complete"` |  |
| iamConfig.clients[0].redirect_uris[1] | string | `"http://wms-diracx:8000/api/auth/authorize/complete"` |  |
| iamConfig.clients[0].scopes[0] | string | `"scim:write"` |  |
| iamConfig.clients[0].scopes[1] | string | `"scim:read"` |  |
| iamConfig.clients[0].scopes[2] | string | `"offline_access"` |  |
| iamConfig.clients[0].scopes[3] | string | `"openid"` |  |
| iamConfig.clients[0].scopes[4] | string | `"profile"` |  |
| iamConfig.clients[0].scopes[5] | string | `"iam:admin.write"` |  |
| iamConfig.clients[0].scopes[6] | string | `"iam:admin.read"` |  |
| iamConfig.groups.dirac_admin.user[0] | string | `"dpps_user"` |  |
| iamConfig.groups.dirac_user.user[0] | string | `"test_user"` |  |
| iamConfig.groups.dpps_genpilot.user[0] | string | `"dpps_user"` |  |
| iamConfig.groups.dpps_group.user[0] | string | `"dpps_user"` |  |
| iamConfig.groups.dpps_group.user[1] | string | `"test_user"` |  |
| iamConfig.issuer | string | `"http://wms-dpps-iam-login-service:8080"` |  |
| iamConfig.users[0].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| iamConfig.users[0].cert.env_var | string | `"X509_USER_CERT"` |  |
| iamConfig.users[0].cert.kind | string | `"env_var_file"` |  |
| iamConfig.users[0].email | string | `"dpps@test.example"` |  |
| iamConfig.users[0].family_name | string | `"User"` |  |
| iamConfig.users[0].given_name | string | `"DPPS"` |  |
| iamConfig.users[0].groups[0] | string | `"ctao.dpps.test"` |  |
| iamConfig.users[0].groups[1] | string | `"dpps_group"` |  |
| iamConfig.users[0].groups[2] | string | `"dpps_genpilot"` |  |
| iamConfig.users[0].groups[3] | string | `"dirac_admin"` |  |
| iamConfig.users[0].groups[4] | string | `"dirac_user"` |  |
| iamConfig.users[0].password | string | `"dpps-password"` |  |
| iamConfig.users[0].role | string | `"ROLE_USER"` |  |
| iamConfig.users[0].subject_dn | string | `"DPPS User"` |  |
| iamConfig.users[0].username | string | `"dpps_user"` |  |
| iamConfig.users[1].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| iamConfig.users[1].cert.env_var | string | `"X509_USER_CERT"` |  |
| iamConfig.users[1].cert.kind | string | `"env_var_file"` |  |
| iamConfig.users[1].email | string | `"dpps@test.example"` |  |
| iamConfig.users[1].family_name | string | `"User"` |  |
| iamConfig.users[1].given_name | string | `"TestDpps"` |  |
| iamConfig.users[1].groups[0] | string | `"ctao.dpps.test"` |  |
| iamConfig.users[1].groups[1] | string | `"dpps_group"` |  |
| iamConfig.users[1].groups[2] | string | `"dirac_user"` |  |
| iamConfig.users[1].password | string | `"test-password"` |  |
| iamConfig.users[1].role | string | `"ROLE_USER"` |  |
| iamConfig.users[1].subject_dn | string | `"DPPS User"` |  |
| iamConfig.users[1].username | string | `"test_user"` |  |
| iamConfig.users[2].email | string | `"dpps@test.example"` |  |
| iamConfig.users[2].family_name | string | `"User"` |  |
| iamConfig.users[2].given_name | string | `"TestAdmin"` |  |
| iamConfig.users[2].groups[0] | string | `"ctao.dpps.test"` |  |
| iamConfig.users[2].password | string | `"test-password"` |  |
| iamConfig.users[2].role | string | `"ROLE_ADMIN"` |  |
| iamConfig.users[2].username | string | `"admin-user"` |  |
| iam_external.enabled | bool | `false` |  |
| image | object | `{"pullPolicy":"IfNotPresent","repository_prefix":"harbor.cta-observatory.org/dpps/wms","tag":null}` | Image settings. |
| image.repository_prefix | string | `"harbor.cta-observatory.org/dpps/wms"` | Prefix of the repository, pods will use <repository_prefix>-{server,client,ce} |
| image.tag | string | `nil` | Image tag, if not set, the chart's appVersion will be used |
| imagePullSecrets | list | `[{"name":"harbor-pull-secret"}]` | Secrets needed to access image registries |
| mariadb | object | `{"auth":{"rootPassword":"dirac-db-root"},"enabled":true,"global":{"security":{"allowInsecureImages":true}},"image":{"registry":"harbor.cta-observatory.org/proxy_cache","repository":"bitnamilegacy/mariadb"},"initdbScripts":{"create-user.sql":"CREATE USER IF NOT EXISTS 'Dirac'@'%' IDENTIFIED BY 'dirac-db';\nCREATE USER IF NOT EXISTS 'indigo-iam'@'%' IDENTIFIED BY 'PassW0rd';\nCREATE DATABASE IF NOT EXISTS `indigo-iam`;\nGRANT ALL PRIVILEGES ON `indigo-iam`.* TO `indigo-iam`@`%`;\nFLUSH PRIVILEGES;\n"}}` | Configuration for the bitnami mariadb subchart. Disable if DIRAC database is provided externally. |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| resources | object | `{}` |  |
| rucio.enabled | bool | `false` |  |
| rucio.rucioConfig | string | `nil` |  |
| service.port | int | `8080` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations | object | `{}` | Annotations to add to the service account |
| serviceAccount.automount | bool | `true` | Automatically mount a ServiceAccount's API credentials? |
| serviceAccount.create | bool | `true` | Specifies whether a service account should be created |
| serviceAccount.name | string | `""` | If not set and create is true, a name is generated using the fullname template |
| test_ce | object | `{"enabled":true,"resources":{}}` | A simple SSH compute element for testing |
| tolerations | list | `[]` |  |
| volumeMounts | list | `[]` |  |
| volumes | list | `[]` |  |
| waitForLoginService.image.pullPolicy | string | `"IfNotPresent"` |  |
| waitForLoginService.image.repository | string | `"almalinux"` |  |
| waitForLoginService.image.tag | int | `9` |  |

