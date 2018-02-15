package volume

// ----------------------------------------------------------------------------
// DO NOT EDIT THIS FILE
// This file was generated by `swagger generate operation`
//
// See hack/swagger-gen.sh
// ----------------------------------------------------------------------------

import "github.com/docker/docker/api/types"

// VolumesListOKBody volumes list o k body
// swagger:model VolumesListOKBody
type VolumesListOKBody struct {

	// List of volumes
	// Required: true
	Volumes []*types.Volume `json:"Volumes"`

	// Warnings that occurred when fetching the list of volumes
	// Required: true
	Warnings []string `json:"Warnings"`
}
