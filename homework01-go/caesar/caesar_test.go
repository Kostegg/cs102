package caesar

import "testing"

func TestEncryptCaesar(t *testing.T) {
	result := EncryptCaesar("PYTHON", 3)
<<<<<<< HEAD
	expectedResult := "SBWKRQ"

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
	}

	result = EncryptCaesar("python", 3)
	expectedResult = "sbwkrq"

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
	}

	result = EncryptCaesar("Python3.6", 3)
	expectedResult = "Sbwkrq3.6"

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
	}

	result = EncryptCaesar("", 3)
	expectedResult = ""

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
=======
	expected_result := "SBWKRQ"

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
	}

	result = EncryptCaesar("python", 3)
	expected_result = "sbwkrq"

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
	}

	result = EncryptCaesar("Python3.6", 3)
	expected_result = "Sbwkrq3.6"

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
	}

	result = EncryptCaesar("", 3)
	expected_result = ""

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
>>>>>>> daaaf63... Initial commit
	}
}

func TestDecryptCaesar(t *testing.T) {
	result := DecryptCaesar("SBWKRQ", 3)
<<<<<<< HEAD
	expectedResult := "PYTHON"

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
	}

	result = DecryptCaesar("sbwkrq", 3)
	expectedResult = "python"

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
	}

	result = DecryptCaesar("Sbwkrq3.6", 3)
	expectedResult = "Python3.6"

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
	}

	result = DecryptCaesar("", 3)
	expectedResult = ""

	if result != expectedResult {
		t.Fatalf("Expected '%s' but got '%s'", expectedResult, result)
=======
	expected_result := "PYTHON"

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
	}

	result = DecryptCaesar("sbwkrq", 3)
	expected_result = "python"

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
	}

	result = DecryptCaesar("Sbwkrq3.6", 3)
	expected_result = "Python3.6"

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
	}

	result = DecryptCaesar("", 3)
	expected_result = ""

	if result != expected_result {
		t.Fatalf("Expected '%s' but got '%s'", expected_result, result)
>>>>>>> daaaf63... Initial commit
	}
}
