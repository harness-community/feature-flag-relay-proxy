data "harness_platform_organization" "Harness_Community" {
  identifier = "Harness_Community"
  name       = "Harness_Community"
}

data "harness_platform_project" "Feature_Flags" {
  name   = "Feature_Flags"
  org_id = "Feature_Flags"
}


resource "harness_platform_service" "feature_flag_relay_proxy" {
  identifier = "feature_flag_relay_proxy"
  name       = "feature_flag_relay_proxy"
  org_id     = data.harness_platform_organization.Harness_Community.id
  project_id = data.harness_platform_project.Feature_Flags.id
  yaml       = file("${path.module}/service.yaml")
}