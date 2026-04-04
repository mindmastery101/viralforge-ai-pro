from app import generate_viral_script

def test_generate_script():
    script = generate_viral_script("Test topic")
    assert len(script) > 0
    print("✅ Script generated successfully!")
