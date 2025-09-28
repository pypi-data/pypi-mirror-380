"""
Advanced WireViz Prompt System for Circuit Diagram Generation
Provides intelligent, guided prompts for creating professional circuit diagrams
"""

from fastmcp.contrib.mcp_mixin import MCPMixin, mcp_prompt
from fastmcp import Context
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
import logging

try:
    from fastmcp.contrib.elicitation import (
        mcp_elicitation,
        QuestionType,
        ElicitationContext
    )
    ELICITATION_AVAILABLE = True
except ImportError:
    ELICITATION_AVAILABLE = False

log = logging.getLogger(__name__)


class CircuitComponent(BaseModel):
    """Represents a circuit component with specifications"""
    name: str
    type: str  # "microcontroller", "sensor", "actuator", "display", etc.
    pins: List[str]
    power_requirements: Optional[str] = None
    description: Optional[str] = None


class WiringConnection(BaseModel):
    """Represents a wiring connection between components"""
    from_component: str
    from_pin: str
    to_component: str
    to_pin: str
    wire_color: Optional[str] = None
    wire_gauge: Optional[str] = None


class CircuitSpecification(BaseModel):
    """Complete circuit specification for WireViz generation"""
    project_name: str
    description: str
    components: List[CircuitComponent]
    connections: List[WiringConnection]
    power_supply: str
    notes: Optional[List[str]] = None


class WireVizPrompts(MCPMixin):
    """Advanced prompts for guided WireViz circuit creation"""

    def __init__(self, config):
        self.config = config

    @mcp_prompt
    async def circuit_assistant(
        self,
        project_type: str = Field(description="Type of project (sensor_monitoring, home_automation, robotics, iot_device, led_effects, motor_control)"),
        skill_level: str = Field(description="Your experience level (beginner, intermediate, advanced)"),
        components_available: str = Field(default="", description="Components you have available (comma-separated list)")
    ) -> str:
        """Interactive circuit design assistant"""

        component_suggestions = self._get_project_components(project_type)
        skill_guidance = self._get_skill_guidance(skill_level)

        return f"""# 🔌 Circuit Design Assistant

## Project: {project_type.title().replace('_', ' ')}

### 📋 Recommended Components for {project_type}:
{component_suggestions}

### 🎯 Guidance for {skill_level} Level:
{skill_guidance}

### 🔧 Component Analysis:
{self._analyze_available_components(components_available) if components_available else "No components specified - I'll suggest a complete parts list"}

### ⚡ Next Steps:
1. **Confirm your component selection**
2. **Specify your Arduino board** (Uno, Nano, ESP32, etc.)
3. **Describe the specific functionality** you want to achieve
4. **I'll generate a professional wiring diagram** with proper wire colors, pin assignments, and safety considerations

### 💡 Pro Tips:
- **Wire Colors**: I'll use standard colors (Red: 5V, Black: GND, etc.)
- **Pin Selection**: I'll choose optimal pins for your components (PWM for LEDs, interrupt pins for sensors)
- **Power Management**: I'll include proper power distribution and decoupling
- **Safety**: All connections will follow electrical safety standards

**Ready to design your circuit? Just tell me more about what you want to build!**
"""

    @mcp_prompt
    async def sensor_circuit_builder(
        self,
        sensor_types: str = Field(description="Types of sensors (temperature, humidity, pressure, light, motion, distance, etc.)"),
        data_output: str = Field(description="How to output data (serial_monitor, lcd_display, sd_card, wifi_cloud, all)"),
        power_source: str = Field(default="usb", description="Power source (usb, battery, solar, mains)")
    ) -> str:
        """Specialized sensor circuit building prompt"""

        sensors = [s.strip() for s in sensor_types.split(',')]
        outputs = [o.strip() for o in data_output.split(',')]

        sensor_specs = self._get_sensor_specifications(sensors)
        output_components = self._get_output_components(outputs)
        power_design = self._get_power_design(power_source)

        return f"""# 📊 Professional Sensor Monitoring Circuit

## 🎯 Project Overview
**Sensors**: {', '.join(sensors)}
**Data Output**: {', '.join(outputs)}
**Power Source**: {power_source}

## 🔬 Sensor Specifications
{sensor_specs}

## 📺 Output Components
{output_components}

## ⚡ Power Design
{power_design}

## 🧩 Intelligent Pin Assignment
I'll automatically assign pins based on sensor requirements:
- **Analog Sensors** → A0-A5 (with proper voltage dividers if needed)
- **Digital Sensors** → Digital pins with pullups where required
- **I2C Devices** → SDA/SCL with pullup resistors
- **SPI Devices** → Hardware SPI pins for maximum speed
- **PWM Outputs** → PWM-capable pins for any analog outputs

## 📐 Circuit Features I'll Include
- ✅ **Proper Pull-up/Pull-down Resistors** for digital signals
- ✅ **Decoupling Capacitors** for stable power
- ✅ **Level Shifters** if mixing 3.3V and 5V components
- ✅ **Protection Diodes** for inductive loads
- ✅ **Clear Wire Labeling** with standard color coding
- ✅ **Professional Connector Layout** for easy assembly

**Describe your specific measurement requirements and I'll generate a production-ready wiring diagram!**
"""

    @mcp_prompt
    async def iot_device_designer(
        self,
        device_purpose: str = Field(description="What the IoT device does (weather_station, plant_monitor, security_system, etc.)"),
        connectivity: str = Field(description="Connection type (wifi, bluetooth, lora, cellular)"),
        deployment_location: str = Field(default="indoor", description="Where it will be used (indoor, outdoor, mobile, fixed)")
    ) -> str:
        """IoT device circuit design prompt"""

        connectivity_specs = self._get_connectivity_specs(connectivity)
        environmental_considerations = self._get_environmental_specs(deployment_location)
        iot_components = self._get_iot_components(device_purpose)

        return f"""# 🌐 Professional IoT Device Circuit Design

## 📡 IoT Device: {device_purpose.title().replace('_', ' ')}
**Connectivity**: {connectivity.upper()}
**Environment**: {deployment_location.title()}

## 🔗 Connectivity Specifications
{connectivity_specs}

## 🏠 Environmental Considerations
{environmental_considerations}

## 🧰 Recommended IoT Components
{iot_components}

## 🔋 Smart Power Management
For IoT devices, I'll design efficient power management:
- **Sleep Modes** between sensor readings
- **Voltage Regulation** for stable operation
- **Battery Monitoring** with low-voltage alerts
- **Charging Circuits** for rechargeable systems

## 📊 Data Flow Architecture
1. **Sensor Reading** → Microcontroller
2. **Local Processing** → Data validation and filtering
3. **Connectivity Module** → WiFi/Bluetooth/LoRa transmission
4. **Cloud Integration** → MQTT, HTTP, or custom protocols
5. **Local Display** → Status indication and diagnostics

## 🛡️ Production Features I'll Include
- ✅ **Antenna Placement** for optimal signal strength
- ✅ **EMI Protection** with proper grounding
- ✅ **Watchdog Circuits** for reliable operation
- ✅ **Debug Interfaces** for troubleshooting
- ✅ **Status LEDs** for visual feedback
- ✅ **Reset Buttons** for manual recovery

**Tell me your specific IoT requirements and I'll create a professional, production-ready circuit diagram!**
"""

    @mcp_prompt
    async def motor_control_expert(
        self,
        motor_types: str = Field(description="Types of motors (servo, stepper, dc_motor, brushless, linear_actuator)"),
        control_precision: str = Field(description="Required precision (basic_positioning, precise_positioning, speed_control, torque_control)"),
        safety_features: str = Field(default="", description="Required safety features (emergency_stop, current_limiting, encoder_feedback, thermal_protection)")
    ) -> str:
        """Motor control circuit design expert"""

        motors = [m.strip() for m in motor_types.split(',')]
        motor_specs = self._get_motor_specifications(motors)
        precision_requirements = self._get_precision_specs(control_precision)
        safety_circuits = self._get_safety_circuits(safety_features)

        return f"""# ⚙️ Professional Motor Control Circuit Design

## 🔧 Motor Configuration
**Motor Types**: {', '.join(motors)}
**Control Precision**: {control_precision.replace('_', ' ').title()}
**Safety Features**: {safety_features.replace('_', ' ').title() if safety_features else 'Basic'}

## 🎛️ Motor Driver Specifications
{motor_specs}

## 🎯 Precision Control Requirements
{precision_requirements}

## 🛡️ Safety Circuit Design
{safety_circuits}

## ⚡ Power Distribution Design
For motor control, I'll design robust power systems:
- **Separate Motor Power** from logic power (prevents noise)
- **Current Limiting** circuits to protect motors and drivers
- **Flyback Diodes** for inductive load protection
- **Capacitor Banks** for motor start-up current
- **Emergency Stop** circuits with fail-safe operation

## 📐 Advanced Control Features
- ✅ **PWM Speed Control** with proper frequencies
- ✅ **Direction Control** with H-bridge circuits
- ✅ **Encoder Interfaces** for position feedback
- ✅ **Current Sensing** for load monitoring
- ✅ **Thermal Management** with temperature monitoring
- ✅ **Communication Buses** (CAN, RS485) for complex systems

## 🔍 Professional Motor Control Features
- **Smooth Acceleration/Deceleration** profiles
- **Stall Detection** and recovery
- **Position Homing** sequences
- **Multi-axis Coordination** for complex movements
- **Real-time Control** with interrupt-driven timing

**Describe your specific motor control application and I'll generate an industrial-grade control circuit!**
"""

    def _get_project_components(self, project_type: str) -> str:
        """Get component suggestions based on project type"""
        components_db = {
            "sensor_monitoring": """
• **Arduino Uno/Nano** - Main microcontroller
• **DHT22** - Temperature/humidity sensor
• **BMP280** - Pressure sensor
• **16x2 LCD** - Data display
• **SD Card Module** - Data logging
• **RTC Module** - Timestamping
• **Breadboard & Jumper Wires**""",

            "home_automation": """
• **ESP32/ESP8266** - WiFi-enabled microcontroller
• **Relay Modules** - Control AC devices
• **PIR Motion Sensor** - Occupancy detection
• **Light Sensor (LDR)** - Ambient light
• **Temperature Sensor** - Climate control
• **OLED Display** - Status indication
• **Push Buttons** - Manual controls""",

            "robotics": """
• **Arduino Mega** - Multiple pin requirements
• **Servo Motors** - Precise positioning
• **Ultrasonic Sensor (HC-SR04)** - Distance measurement
• **Motor Driver (L298N)** - DC motor control
• **IMU/Gyroscope** - Orientation sensing
• **Wheel Encoders** - Position feedback
• **Bluetooth Module** - Remote control""",

            "iot_device": """
• **ESP32** - Built-in WiFi and Bluetooth
• **Various Sensors** - Based on application
• **OLED Display** - Local status
• **Deep Sleep Circuit** - Battery efficiency
• **Voltage Regulator** - Stable power
• **Antenna** - Signal optimization
• **Capacitive Touch** - User interface""",

            "led_effects": """
• **Arduino Nano** - Compact form factor
• **WS2812B LED Strip** - Addressable RGB LEDs
• **Potentiometer** - Brightness control
• **Push Buttons** - Effect selection
• **Power Supply** - Adequate current capacity
• **Level Shifter** - 3.3V to 5V logic
• **Capacitors** - Power smoothing""",

            "motor_control": """
• **Arduino Uno/Mega** - Based on motor count
• **Motor Drivers** - Appropriate for motor type
• **Encoders** - Position feedback
• **Current Sensors** - Load monitoring
• **Emergency Stop** - Safety circuit
• **Power Supply** - Motor voltage/current
• **Heat Sinks** - Thermal management"""
        }
        return components_db.get(project_type, "• Custom component selection based on your requirements")

    def _get_skill_guidance(self, skill_level: str) -> str:
        """Provide skill-appropriate guidance"""
        guidance = {
            "beginner": """
**🟢 Beginner-Friendly Approach:**
• I'll use **pre-made modules** instead of discrete components
• **Clear wire colors** with detailed labeling
• **Step-by-step assembly** instructions
• **Safety reminders** for handling electronics
• **Troubleshooting tips** for common issues
• **Simple code examples** to get started""",

            "intermediate": """
**🟡 Intermediate Level Features:**
• **Optimized pin assignments** for efficiency
• **Custom PCB layout** suggestions
• **Performance considerations** and timing
• **Component alternatives** and trade-offs
• **Debugging interfaces** built into the design
• **Modular design** for easy modifications""",

            "advanced": """
**🔴 Advanced Engineering Features:**
• **Professional schematic** symbols and standards
• **Signal integrity** considerations
• **EMI/EMC compliance** design practices
• **Thermal management** calculations
• **Production testing** interfaces
• **Cost optimization** and sourcing recommendations"""
        }
        return guidance.get(skill_level, guidance["intermediate"])

    def _analyze_available_components(self, components: str) -> str:
        """Analyze user's available components"""
        if not components:
            return ""

        component_list = [c.strip() for c in components.split(',')]

        analysis = "**📦 Your Available Components Analysis:**\n"
        for component in component_list:
            analysis += f"• **{component}** - I'll optimize the circuit design around this\n"

        analysis += "\n**🔧 I'll suggest:**\n"
        analysis += "• Additional components needed to complete the circuit\n"
        analysis += "• Alternative uses for components you might not have considered\n"
        analysis += "• Optimal pin assignments for your specific component mix\n"

        return analysis

    def _get_sensor_specifications(self, sensors: List[str]) -> str:
        """Get detailed specifications for sensors"""
        # This would be expanded with a comprehensive sensor database
        specs = "**Sensor Technical Specifications:**\n"
        for sensor in sensors:
            specs += f"• **{sensor.title()}**: I'll include proper interface circuits, calibration notes, and optimal placement\n"
        return specs

    def _get_output_components(self, outputs: List[str]) -> str:
        """Get output component specifications"""
        specs = "**Output Interface Design:**\n"
        for output in outputs:
            specs += f"• **{output.replace('_', ' ').title()}**: Professional interface with proper signal conditioning\n"
        return specs

    def _get_power_design(self, power_source: str) -> str:
        """Get power design specifications"""
        power_designs = {
            "usb": "**USB Power (5V)**: Clean, regulated power with USB protection",
            "battery": "**Battery Power**: Efficient voltage regulation with low-power design",
            "solar": "**Solar Power**: Charge controller with battery backup system",
            "mains": "**Mains Power**: Isolated transformer with proper safety circuits"
        }
        return power_designs.get(power_source, "Custom power design based on requirements")

    def _get_connectivity_specs(self, connectivity: str) -> str:
        """Get connectivity specifications"""
        return f"**{connectivity.upper()} Implementation**: Professional antenna design with optimal signal routing"

    def _get_environmental_specs(self, location: str) -> str:
        """Get environmental specifications"""
        return f"**{location.title()} Deployment**: Weather protection and environmental considerations included"

    def _get_iot_components(self, purpose: str) -> str:
        """Get IoT-specific components"""
        return f"**{purpose.replace('_', ' ').title()} Components**: Optimized sensor and actuator selection"

    def _get_motor_specifications(self, motors: List[str]) -> str:
        """Get motor specifications"""
        specs = "**Motor Driver Selection:**\n"
        for motor in motors:
            specs += f"• **{motor.replace('_', ' ').title()}**: Appropriate driver with current/voltage ratings\n"
        return specs

    def _get_precision_specs(self, precision: str) -> str:
        """Get precision requirements"""
        return f"**{precision.replace('_', ' ').title()}**: Encoder feedback and control algorithms included"

    def _get_safety_circuits(self, features: str) -> str:
        """Get safety circuit specifications"""
        if not features:
            return "**Basic Safety**: Overcurrent protection and thermal monitoring"
        return f"**Safety Features**: {features.replace('_', ' ').title()} circuits included"

    # ============================================================================
    # ELICITATION-BASED CIRCUIT DESIGNER (Interactive Engineering Interview)
    # ============================================================================

    if ELICITATION_AVAILABLE:
        @mcp_elicitation(
            name="circuit_design_interview",
            description="Professional circuit design interview - I'll ask you questions like a seasoned engineer to create the perfect wiring diagram",
            flow=[
                {
                    "id": "project_overview",
                    "question": "🎯 What kind of project are you building? Describe the main functionality you want to achieve.",
                    "type": QuestionType.TEXT,
                    "required": True
                },
                {
                    "id": "experience_level",
                    "question": "🎓 What's your experience level with electronics?",
                    "type": QuestionType.CHOICE,
                    "choices": [
                        "🟢 Beginner - New to Arduino and electronics",
                        "🟡 Intermediate - Built a few projects, comfortable with basics",
                        "🔴 Advanced - Experienced with PCB design and complex circuits",
                        "🎓 Professional - I design circuits for a living"
                    ],
                    "required": True
                },
                {
                    "id": "board_selection",
                    "question": "🔧 Which Arduino board are you using (or planning to use)?",
                    "type": QuestionType.CHOICE,
                    "choices": [
                        "Arduino Uno - Great for learning and prototyping",
                        "Arduino Nano - Compact for finished projects",
                        "ESP32 - Need WiFi/Bluetooth connectivity",
                        "ESP8266 - Simple WiFi projects",
                        "Arduino Mega - Need lots of pins",
                        "Custom/Other - I'll specify details"
                    ],
                    "required": True
                },
                {
                    "id": "components_list",
                    "question": "📦 What components do you want to include? List everything you have or plan to use (sensors, displays, motors, etc.)",
                    "type": QuestionType.TEXT,
                    "required": True
                },
                {
                    "id": "power_requirements",
                    "question": "⚡ How will you power this project?",
                    "type": QuestionType.CHOICE,
                    "choices": [
                        "USB - Powered from computer/USB adapter",
                        "Battery - Portable operation (specify type if known)",
                        "Wall Adapter - Plugged into mains power",
                        "Solar - Self-sustaining outdoor project",
                        "Mixed - Multiple power sources",
                        "Not sure - I need guidance"
                    ],
                    "required": True
                },
                {
                    "id": "environmental_needs",
                    "question": "🏠 Where will this project operate?",
                    "type": QuestionType.CHOICE,
                    "choices": [
                        "Indoor - Controlled environment",
                        "Outdoor - Weather resistance needed",
                        "Mobile - Will be carried/moved frequently",
                        "Industrial - Harsh environment, vibration",
                        "Laboratory - Precision measurement environment"
                    ],
                    "required": True
                },
                {
                    "id": "special_requirements",
                    "question": "🎯 Any special requirements? (Check all that apply)",
                    "type": QuestionType.MULTI_CHOICE,
                    "choices": [
                        "🔒 Safety-critical - Cannot fail",
                        "🔋 Battery efficiency - Must run for weeks/months",
                        "⚡ High speed - Fast response times needed",
                        "🎛️ Precise control - Accurate positioning/measurement",
                        "📡 Remote monitoring - Need connectivity",
                        "🔧 Easy maintenance - Simple component replacement",
                        "💰 Cost optimization - Keep component costs low",
                        "📐 Compact size - Space constraints"
                    ],
                    "required": False
                },
                {
                    "id": "interface_preferences",
                    "question": "👥 How do you want to interact with this project?",
                    "type": QuestionType.MULTI_CHOICE,
                    "choices": [
                        "🖥️ Serial Monitor - Debug via computer",
                        "📱 Mobile App - Phone/tablet control",
                        "🖲️ Physical Controls - Buttons, knobs, switches",
                        "📺 Local Display - LCD/OLED screen",
                        "🌐 Web Interface - Browser-based control",
                        "🔊 Voice Control - Audio commands",
                        "🎮 Remote Control - IR/RF remote",
                        "🤖 Autonomous - No human interaction needed"
                    ],
                    "required": False
                },
                {
                    "id": "skill_building",
                    "question": "📚 What would you like to learn from this project?",
                    "type": QuestionType.MULTI_CHOICE,
                    "choices": [
                        "🔌 Basic wiring and connections",
                        "📊 Sensor data collection and processing",
                        "⚙️ Motor control and robotics",
                        "📡 Wireless communication (WiFi, Bluetooth)",
                        "💾 Data logging and storage",
                        "🎨 User interface design",
                        "🔋 Power management optimization",
                        "🛡️ Safety and protection circuits"
                    ],
                    "required": False
                }
            ]
        )
        async def circuit_design_interview(
            self,
            ctx: ElicitationContext
        ) -> str:
            """Professional circuit design interview that creates custom wiring diagrams"""

            # Extract all the interview responses
            project = ctx.get_response("project_overview")
            experience = ctx.get_response("experience_level")
            board = ctx.get_response("board_selection")
            components = ctx.get_response("components_list")
            power = ctx.get_response("power_requirements")
            environment = ctx.get_response("environmental_needs")
            special_reqs = ctx.get_response("special_requirements", [])
            interfaces = ctx.get_response("interface_preferences", [])
            learning_goals = ctx.get_response("skill_building", [])

            # Generate professional analysis
            analysis = self._generate_professional_analysis(
                project, experience, board, components, power,
                environment, special_reqs, interfaces, learning_goals
            )

            # Use sampling to generate AI-powered analysis and WireViz YAML
            try:
                # Check if context supports sampling for AI-enhanced response
                if hasattr(ctx, 'sample') and callable(ctx.sample):
                    # Create comprehensive prompt for AI analysis
                    sampling_prompt = self._create_sampling_prompt(
                        project, experience, board, components, power,
                        environment, special_reqs, interfaces, learning_goals
                    )

                    # Get AI-generated analysis and circuit design
                    ai_response = await ctx.sample(sampling_prompt)

                    if ai_response and hasattr(ai_response, 'content'):
                        # Extract AI response content
                        ai_content = ai_response.content

                        # Combine structured interview data with AI insights
                        return f"""# 🎯 AI-Enhanced Professional Circuit Design

## 📋 Interview Summary
**Project**: {project}
**Experience**: {experience}
**Board**: {board}
**Environment**: {environment}
**Power**: {power}

---

{ai_content}

---

## 🔧 Implementation Ready
Your circuit design is now ready for implementation! The AI analysis above includes:
- ✅ **Custom component recommendations** based on your specific requirements
- ✅ **Intelligent pin assignments** optimized for your board and components
- ✅ **Power system design** tailored to your environment and usage
- ✅ **Professional wiring diagram** with industry-standard practices

**Next Step**: Use the WireViz YAML provided above with `wireviz_generate_from_yaml` to create your professional circuit diagram!

*This analysis combines structured engineering interview data with AI-powered circuit design intelligence.*
"""

            except Exception as e:
                # Log the sampling attempt failure but continue with fallback
                import logging
                logger = logging.getLogger(__name__)
                logger.debug(f"Sampling failed in elicitation response: {e}")

            # Fallback to structured analysis when sampling unavailable
            analysis = self._generate_professional_analysis(
                project, experience, board, components, power,
                environment, special_reqs, interfaces, learning_goals
            )

            # Create the comprehensive circuit design plan
            return f"""# 🎯 Professional Circuit Design Analysis

## 📋 Project Summary
**Project**: {project}
**Experience Level**: {experience}
**Board**: {board}
**Environment**: {environment}
**Power**: {power}

## 🔬 Engineering Analysis
{analysis}

## 📐 Custom Circuit Design Plan

### 🧩 Intelligent Component Integration
Based on your requirements, I've designed an optimal pin assignment strategy:

{self._generate_pin_assignment_strategy(board, components, special_reqs)}

### ⚡ Power Distribution Design
{self._generate_power_design_analysis(power, components, special_reqs)}

### 🛡️ Safety & Protection Circuits
{self._generate_safety_analysis(environment, special_reqs)}

### 📊 Signal Integrity Considerations
{self._generate_signal_integrity_analysis(board, components, environment)}

## 🎨 Professional Features Included

### 🔧 Circuit Design Excellence
- ✅ **Industry-standard wire colors** (Red: 5V, Black: GND, etc.)
- ✅ **Proper pull-up/pull-down resistors** for all digital inputs
- ✅ **Decoupling capacitors** for stable power distribution
- ✅ **Protection diodes** for inductive loads (motors, relays)
- ✅ **Current limiting resistors** for LEDs and sensitive components
- ✅ **EMI suppression** techniques for clean signals

### 📚 Educational Value
{self._generate_learning_content(learning_goals, experience)}

### 🔧 Assembly & Debugging
- 📝 **Step-by-step assembly** instructions
- 🔍 **Built-in test points** for troubleshooting
- ⚡ **Status LEDs** for power and activity indication
- 🔄 **Modular design** for easy component swapping

## 🚀 Next Steps

I'm ready to generate your professional wiring diagram! Here's what you'll get:

1. **📐 Detailed Circuit Diagram** - Professional WireViz schematic
2. **🎨 Color-coded Wiring** - Industry-standard wire colors
3. **📋 Component List** - Exact part numbers and specifications
4. **⚡ Assembly Instructions** - Step-by-step build guide
5. **🔧 Testing Procedures** - Validation and troubleshooting

**Ready to see your custom circuit design? Just say "Generate my circuit diagram" and I'll create a production-ready wiring diagram based on this analysis!**

---
*This analysis was generated through professional engineering interview techniques, ensuring your circuit meets industrial standards while matching your specific requirements and skill level.*
"""

        def _generate_professional_analysis(self, project, experience, board, components, power, environment, special_reqs, interfaces, learning_goals):
            """Generate professional engineering analysis"""

            # Extract experience level for targeted analysis
            exp_level = "beginner" if "Beginner" in experience else "intermediate" if "Intermediate" in experience else "advanced"

            analysis = f"""
**🎯 Project Scope Analysis:**
Your {project.lower()} project requires careful consideration of component integration and power management. Based on your {exp_level} experience level, I'll design a circuit that challenges you appropriately while ensuring reliability.

**🔧 Component Integration Strategy:**
{self._analyze_component_complexity(components, exp_level)}

**⚡ Power & Performance Requirements:**
{self._analyze_power_requirements(power, components, special_reqs)}

**🛡️ Environmental Considerations:**
{self._analyze_environmental_factors(environment, special_reqs)}
"""
            return analysis

        def _analyze_component_complexity(self, components, exp_level):
            """Analyze component integration complexity"""
            component_count = len(components.split(','))

            if exp_level == "beginner":
                return f"With {component_count} components, I'll use pre-made modules and clear documentation to ensure successful assembly."
            elif exp_level == "intermediate":
                return f"Your {component_count}-component design allows for optimization techniques like shared power rails and efficient pin usage."
            else:
                return f"The {component_count}-component system enables advanced features like signal conditioning and professional layout practices."

        def _analyze_power_requirements(self, power, components, special_reqs):
            """Analyze power system requirements"""
            if "Battery" in power:
                return "Battery operation requires efficient power management, sleep modes, and voltage regulation circuits."
            elif "Solar" in power:
                return "Solar power needs charge controller circuits, battery backup, and power monitoring systems."
            else:
                return "Stable power design with proper filtering and protection circuits for reliable operation."

        def _analyze_environmental_factors(self, environment, special_reqs):
            """Analyze environmental protection needs"""
            if "Outdoor" in environment:
                return "Outdoor deployment requires weatherproof connectors, moisture protection, and temperature compensation."
            elif "Industrial" in environment:
                return "Industrial environment needs vibration resistance, EMI shielding, and robust connector systems."
            else:
                return "Standard indoor protection with basic EMI considerations and thermal management."

        def _generate_pin_assignment_strategy(self, board, components, special_reqs):
            """Generate intelligent pin assignment strategy"""
            return f"""
**📍 Optimized Pin Assignment for {board}:**

• **Digital I/O Priority**: Emergency stops and safety circuits get priority pins
• **Analog Inputs**: Sensors requiring ADC get A0-A5 with proper reference voltage
• **PWM Outputs**: Motors and LED control on PWM-capable pins (3, 5, 6, 9, 10, 11)
• **Communication**: I2C on dedicated SDA/SCL, SPI on hardware pins for speed
• **Interrupts**: Time-critical sensors on interrupt-capable pins (2, 3)
• **Power Pins**: Dedicated 5V/3.3V distribution with current limiting

This assignment minimizes noise, maximizes performance, and follows Arduino best practices.
"""

        def _generate_power_design_analysis(self, power, components, special_reqs):
            """Generate power system analysis"""
            return f"""
**⚡ Power Distribution Architecture:**

• **Primary Supply**: {power} with appropriate voltage regulation
• **Logic Power**: Clean 5V/3.3V rails with decoupling capacitors
• **Motor Power**: Separate rail to prevent digital circuit noise
• **Current Budget**: Calculated for all components with 20% safety margin
• **Protection**: Fuses, reverse voltage protection, and thermal shutdown
• **Monitoring**: Voltage sensing for battery systems and fault detection
"""

        def _generate_safety_analysis(self, environment, special_reqs):
            """Generate safety circuit analysis"""
            safety_critical = any("Safety-critical" in req for req in special_reqs)

            if safety_critical:
                return """
**🛡️ Safety-Critical Design Features:**
• **Redundant Systems**: Dual safety circuits with independent power
• **Fail-Safe Operation**: Default to safe state on any fault condition
• **Watchdog Circuits**: Automatic reset on system hang or malfunction
• **Emergency Stop**: Hardwired emergency shutdown independent of software
• **Status Monitoring**: Real-time health monitoring with alarm outputs
"""
            else:
                return """
**🛡️ Standard Safety Features:**
• **Overcurrent Protection**: Fuses and current limiting circuits
• **Thermal Protection**: Temperature monitoring and thermal shutdown
• **Reverse Voltage Protection**: Diode protection on power inputs
• **ESD Protection**: Static discharge protection on all interfaces
"""

        def _generate_signal_integrity_analysis(self, board, components, environment):
            """Generate signal integrity analysis"""
            return f"""
**📊 Signal Quality Optimization:**

• **Wire Routing**: Separate analog and digital grounds with star ground point
• **Noise Suppression**: Ferrite beads on switching circuits and motor lines
• **Impedance Matching**: Proper termination for high-speed digital signals
• **EMI Reduction**: Twisted pair cables for long runs, shielded cables where needed
• **Ground Strategy**: Single-point grounding to prevent ground loops
• **Power Filtering**: LC filters for motor supplies, RC filters for analog references
"""

        def _generate_learning_content(self, learning_goals, experience):
            """Generate educational content based on learning goals"""
            if not learning_goals:
                return "• **Circuit Understanding**: Detailed explanations of each circuit section and component function"

            content = "• **Targeted Learning Modules**:\n"
            for goal in learning_goals:
                if "Basic wiring" in goal:
                    content += "  - Wire gauge selection and color coding standards\n"
                elif "Sensor data" in goal:
                    content += "  - ADC principles and signal conditioning techniques\n"
                elif "Motor control" in goal:
                    content += "  - PWM theory and H-bridge driver circuits\n"
                elif "Wireless" in goal:
                    content += "  - Antenna theory and RF layout considerations\n"
                elif "Power management" in goal:
                    content += "  - Switching regulator design and efficiency optimization\n"

            return content

        def _create_sampling_prompt(self, project, experience, board, components, power, environment, special_reqs, interfaces, learning_goals):
            """Create comprehensive sampling prompt from elicitation responses"""

            # Build comprehensive prompt for AI analysis
            prompt = f"""You are a professional electronics engineer designing a custom Arduino circuit. Based on the following detailed requirements from a professional engineering interview, create a comprehensive circuit design analysis and generate a complete WireViz YAML diagram.

## Project Requirements (from engineering interview):

**Project Type**: {project}
**Experience Level**: {experience}
**Arduino Board**: {board}
**Components**: {components}
**Power Source**: {power}
**Operating Environment**: {environment}
**Special Requirements**: {', '.join(special_reqs) if special_reqs else 'Standard design'}
**User Interfaces**: {', '.join(interfaces) if interfaces else 'Basic interfaces'}
**Learning Goals**: {', '.join(learning_goals) if learning_goals else 'General understanding'}

## Your Task:

1. **Professional Circuit Analysis**: Provide detailed engineering analysis considering:
   - Component integration strategies specific to the experience level
   - Optimal pin assignments for the chosen Arduino board
   - Power distribution design for the specified power source and environment
   - Signal integrity considerations and protection circuits
   - Safety requirements based on environment and special needs

2. **Generate Complete WireViz YAML**: Create production-ready WireViz YAML that includes:
   - All components with proper specifications
   - Optimal pin assignments following Arduino best practices
   - Industry-standard wire colors and routing
   - Appropriate connectors and cable specifications
   - Protection circuits (fuses, diodes, current limiting)
   - Clear labeling and documentation

3. **Implementation Guidance**: Provide:
   - Step-by-step assembly instructions
   - Testing and validation procedures
   - Troubleshooting guidance
   - Educational explanations appropriate for the experience level

## Format your response as:

### Circuit Design Analysis
[Detailed professional analysis based on interview responses]

### WireViz YAML Code
```yaml
[Complete WireViz YAML for the circuit]
```

### Assembly Instructions
[Step-by-step implementation guidance]

### Educational Notes
[Learning content based on specified goals]

Focus on creating a production-ready design that matches the user's experience level while following professional engineering standards."""

            return prompt

    else:
        # Rich prompts for clients without elicitation support
        @mcp_prompt
        async def quick_pinout_designer(
            self,
            components: str = Field(description="Components to connect (e.g., 'ESP32, servo motor, LED strip')"),
            project_type: str = Field(default="general", description="Project type (robotics, iot, sensor, display, motor_control)"),
            experience: str = Field(default="intermediate", description="Your experience level (beginner, intermediate, advanced)")
        ) -> str:
            """Quick pinout and wiring diagram generator"""

            component_list = [c.strip() for c in components.split(',')]
            component_count = len(component_list)

            # Generate experience-appropriate guidance
            if "beginner" in experience.lower():
                complexity_note = "I'll use pre-made modules and provide clear step-by-step instructions."
                safety_emphasis = "**Safety First**: I'll include important safety reminders and common mistake warnings."
            elif "advanced" in experience.lower():
                complexity_note = "I'll optimize for signal integrity and include professional design considerations."
                safety_emphasis = "**Professional Standards**: Following industry best practices for production-ready circuits."
            else:
                complexity_note = "I'll balance clarity with technical depth for your skill level."
                safety_emphasis = "**Best Practices**: Including proper protection circuits and wire management."

            return f"""# ⚡ Quick Pinout Designer

## 🔌 Your Circuit: {components}
**Project Type**: {project_type.title()}
**Components**: {component_count} components to connect
**Experience Level**: {experience.title()}

## 🎯 Design Approach
{complexity_note}

{safety_emphasis}

## 🧩 Smart Pin Assignment Strategy
I'll automatically assign pins based on component requirements:

**🔴 Power Distribution**:
- **5V Rail**: High-current components (servos, LED strips, displays)
- **3.3V Rail**: Low-power sensors and logic-level devices
- **Ground**: Star ground configuration to minimize noise

**📡 Communication Pins**:
- **I2C Devices** → SDA/SCL with proper pull-up resistors (4.7kΩ)
- **SPI Devices** → Hardware SPI pins for maximum speed
- **UART/Serial** → Hardware serial pins when available

**⚡ Special Function Pins**:
- **PWM Control** → PWM-capable pins (3, 5, 6, 9, 10, 11 on Uno)
- **Analog Sensors** → A0-A5 with appropriate voltage dividers
- **Interrupt Pins** → Pins 2 & 3 for time-critical sensors
- **Digital I/O** → Remaining pins with pull-up/pull-down as needed

## 🎨 Professional Features I'll Include
- ✅ **Standard Wire Colors**: Red (5V), Black (GND), Yellow (Data), etc.
- ✅ **Proper Connectors**: Dupont, JST, screw terminals as appropriate
- ✅ **Protection Circuits**: Fuses, diodes, current limiting resistors
- ✅ **Clear Labels**: Component names, pin numbers, voltage levels
- ✅ **Assembly Notes**: Connection order and testing checkpoints

## 🚀 Ready to Generate
**Just say "Generate my pinout diagram" and I'll create a professional WireViz schematic with:**
1. **Optimal pin assignments** for your components
2. **Color-coded wiring** following industry standards
3. **Protection circuits** for safe operation
4. **Assembly instructions** with testing steps
5. **Troubleshooting guide** for common issues

*Professional circuit design made simple - regardless of your experience level!*
"""

        @mcp_prompt
        async def connector_harness_designer(
            self,
            source_device: str = Field(description="Source device/board (e.g., 'Arduino Uno', 'ESP32 DevKit')"),
            target_devices: str = Field(description="Target devices to connect (e.g., 'servo motor, OLED display, temperature sensor')"),
            cable_length: str = Field(default="short", description="Cable length needed (short: <30cm, medium: 30cm-1m, long: >1m)"),
            environment: str = Field(default="indoor", description="Environment (indoor, outdoor, mobile, industrial)")
        ) -> str:
            """Design custom connector harnesses and cable assemblies"""

            targets = [t.strip() for t in target_devices.split(',')]
            target_count = len(targets)

            # Determine cable specifications based on length and environment
            if cable_length == "long" or "outdoor" in environment.lower():
                cable_spec = "**Shielded twisted pair** cables for signal integrity and EMI protection"
                connector_type = "**Weatherproof connectors** (IP65 rated) for reliable outdoor operation"
            elif "industrial" in environment.lower():
                cable_spec = "**Industrial-grade cables** with high flex life and chemical resistance"
                connector_type = "**Rugged connectors** with strain relief and vibration resistance"
            else:
                cable_spec = "**Standard dupont/JST cables** for clean, reliable connections"
                connector_type = "**Standard connectors** with proper strain relief"

            return f"""# 🔌 Custom Connector Harness Designer

## 📡 Harness Specification
**Source**: {source_device}
**Targets**: {target_count} devices → {target_devices}
**Cable Length**: {cable_length.title()}
**Environment**: {environment.title()}

## 🎯 Professional Harness Design

### 📏 Cable Specifications
{cable_spec}

**Wire Gauge Selection**:
- **Power Lines (5V/12V)**: 18-20 AWG for high current (>500mA)
- **Logic Signals**: 22-24 AWG for digital communication
- **Analog Signals**: 24-26 AWG with twisted pair for noise immunity
- **Ground Returns**: Same gauge as power for proper current handling

### 🔗 Connector Strategy
{connector_type}

**Color Coding Standard**:
- 🔴 **Red**: +5V/+12V power
- ⚫ **Black**: Ground (GND)
- 🟡 **Yellow**: Digital data/clock signals
- 🟢 **Green**: Analog sensor signals
- 🔵 **Blue**: Communication lines (SDA/SCL, TX/RX)
- 🟠 **Orange**: PWM/control signals
- 🟣 **Purple**: Enable/reset lines

### ⚡ Smart Harness Features

**🛡️ Built-in Protection**:
- **Inline fuses** on power lines (auto-reset or blade type)
- **ESD protection** on signal lines with TVS diodes
- **Strain relief** at all connector entry points
- **Ferrite cores** on cables >50cm to reduce EMI

**🔧 Modular Design**:
- **Breakout connectors** for easy troubleshooting
- **Test points** at critical signal junctions
- **LED indicators** for power and activity status
- **Keyed connectors** to prevent reverse insertion

**📋 Professional Assembly**:
- **Heat shrink tubing** for insulation and strain relief
- **Cable ties** for neat routing and organization
- **Labels** on both ends with device names and pin functions
- **Documentation** with pinout diagrams and assembly notes

## 🎨 Custom Harness Advantages

✅ **Plug-and-Play**: No breadboard wiring needed
✅ **Reliable**: Industrial-grade connections
✅ **Maintainable**: Modular design for easy servicing
✅ **Professional**: Clean appearance for finished projects
✅ **Debuggable**: Built-in test points and indicators

## 🚀 Ready to Design Your Custom Harness

**Say "Generate my connector harness" and I'll create:**
1. **Detailed wiring diagram** with all connections
2. **Cable assembly instructions** with part numbers
3. **Connector pinout tables** for each device
4. **Testing procedures** to verify correct assembly
5. **Professional documentation** for future reference

*Transform messy breadboard prototypes into clean, professional installations!*
"""

        @mcp_prompt
        async def circuit_troubleshooter(
            self,
            problem_description: str = Field(description="Describe the issue you're experiencing"),
            circuit_components: str = Field(description="Components in your circuit (e.g., 'Arduino Uno, servo, LED, sensor')"),
            symptoms: str = Field(description="What you observe (e.g., 'LED flickers, servo jitters, no sensor readings')")
        ) -> str:
            """Intelligent circuit troubleshooting assistant"""

            components = [c.strip() for c in circuit_components.split(',')]
            symptom_list = [s.strip() for s in symptoms.split(',')]

            # Analyze common issues based on components and symptoms
            power_issues = any(word in symptoms.lower() for word in ['flicker', 'dim', 'restart', 'reset', 'brown'])
            signal_issues = any(word in symptoms.lower() for word in ['jitter', 'noise', 'intermittent', 'random'])
            connection_issues = any(word in symptoms.lower() for word in ['nothing', 'dead', 'no response', 'not working'])

            return f"""# 🔍 Circuit Troubleshooting Assistant

## ⚠️ Problem Analysis
**Issue**: {problem_description}
**Components**: {', '.join(components)}
**Symptoms**: {', '.join(symptom_list)}

## 🎯 Diagnostic Strategy

### 🔴 Primary Diagnosis
{self._generate_primary_diagnosis(power_issues, signal_issues, connection_issues, components)}

### 📊 Systematic Testing Procedure

**Step 1: Power System Verification** ⚡
- Measure voltage at Arduino 5V pin (should be 4.75-5.25V)
- Check current draw with multimeter (compare to component specs)
- Verify all ground connections with continuity test
- Look for voltage drops across long wires (>0.2V indicates undersized wire)

**Step 2: Signal Integrity Check** 📡
- Use oscilloscope/logic analyzer to check digital signals
- Verify pull-up resistors on I2C lines (4.7kΩ typical)
- Check for signal reflections on long cables (>30cm)
- Measure analog signal noise levels and offsets

**Step 3: Component-Specific Tests** 🔧
{self._generate_component_tests(components)}

**Step 4: Environmental Factors** 🌡️
- Check operating temperature ranges for all components
- Verify adequate ventilation for high-power devices
- Look for electromagnetic interference sources nearby
- Ensure stable mechanical connections (no loose wires)

## 🛠️ Common Solutions by Symptom

{self._generate_solutions_by_symptom(symptoms)}

## 🎯 Professional Debugging Tools

**Essential Tools** 🔧:
- **Digital Multimeter**: Voltage, current, resistance, continuity
- **Oscilloscope**: Signal timing, noise, amplitude analysis
- **Logic Analyzer**: Digital protocol debugging (I2C, SPI, UART)
- **Function Generator**: Signal injection for testing inputs

**Advanced Debugging** 🔬:
- **Protocol Analyzers**: Decode I2C, SPI communication errors
- **Thermal Camera**: Identify overheating components
- **EMI Detector**: Find sources of electromagnetic interference
- **Power Supply Analyzer**: Measure ripple, transient response

## 🚀 Next Steps

Based on your symptoms, I recommend starting with the **{self._recommend_first_step(power_issues, signal_issues, connection_issues)}** diagnostic steps.

**Say "Generate troubleshooting checklist" and I'll create a customized step-by-step debugging guide specific to your circuit and symptoms!**

*Professional circuit debugging - from symptoms to solutions!*
"""

        def _generate_primary_diagnosis(self, power_issues, signal_issues, connection_issues, components):
            """Generate primary diagnosis based on symptoms"""
            if power_issues:
                return """
**🔴 POWER SYSTEM ISSUE SUSPECTED**
- Symptoms indicate insufficient power supply or voltage regulation problems
- Common with high-current components like servos, motors, LED strips
- Check power supply capacity and voltage regulation circuits
"""
            elif signal_issues:
                return """
**📡 SIGNAL INTEGRITY ISSUE SUSPECTED**
- Symptoms suggest noise, timing, or communication problems
- Often caused by improper grounding, long cables, or EMI
- Focus on signal quality, grounding, and cable routing
"""
            elif connection_issues:
                return """
**🔌 CONNECTION ISSUE SUSPECTED**
- Symptoms suggest open circuits, wrong pin assignments, or component failure
- Start with basic connectivity and pin assignment verification
- Check solder joints, connector integrity, and component orientation
"""
            else:
                return """
**🎯 COMPREHENSIVE DIAGNOSIS NEEDED**
- Multiple potential causes - systematic approach required
- Begin with power system verification, then move to signals
- Document measurements at each step for pattern analysis
"""

        def _generate_component_tests(self, components):
            """Generate component-specific test procedures"""
            tests = []

            for component in components:
                comp_lower = component.lower()
                if 'servo' in comp_lower:
                    tests.append("- **Servo**: Test with known good PWM signal (1.5ms = center)")
                elif 'sensor' in comp_lower or 'temperature' in comp_lower or 'humidity' in comp_lower:
                    tests.append("- **Sensor**: Verify power, check I2C address scan, test with known values")
                elif 'led' in comp_lower:
                    tests.append("- **LED**: Test with current limiting resistor, check polarity")
                elif 'motor' in comp_lower:
                    tests.append("- **Motor**: Check driver connections, verify PWM signals, test stall current")
                elif 'display' in comp_lower or 'lcd' in comp_lower or 'oled' in comp_lower:
                    tests.append("- **Display**: Verify I2C/SPI connections, check contrast/brightness settings")

            return '\n'.join(tests) if tests else "- **General**: Test each component individually with minimal circuit"

        def _generate_solutions_by_symptom(self, symptoms):
            """Generate solutions organized by symptom"""
            solutions = """
**🔋 Power Problems** (flickering, resets, dim output):
- Add decoupling capacitors (100µF + 0.1µF) near power inputs
- Use separate power supply for high-current components
- Upgrade to thicker gauge wires for power distribution
- Add ferrite cores to reduce switching noise

**📡 Signal Issues** (jitter, noise, intermittent operation):
- Implement proper star grounding topology
- Add pull-up resistors to I2C lines (4.7kΩ)
- Use twisted pair cables for differential signals
- Separate analog and digital ground planes

**🔌 Connection Problems** (dead circuits, no response):
- Verify pin assignments match your code
- Check solder joint quality with magnifying glass
- Test continuity of all connections with multimeter
- Ensure proper component orientation (polarity)
"""
            return solutions

        def _recommend_first_step(self, power_issues, signal_issues, connection_issues):
            """Recommend which diagnostic step to start with"""
            if power_issues:
                return "power system verification"
            elif connection_issues:
                return "basic connectivity testing"
            else:
                return "signal integrity analysis"

        @mcp_prompt
        async def pcb_layout_advisor(
            self,
            circuit_description: str = Field(description="Describe your circuit design"),
            board_size: str = Field(default="medium", description="Preferred board size (small: <5cm, medium: 5-10cm, large: >10cm)"),
            layer_count: str = Field(default="2", description="Number of PCB layers (2, 4, 6+)"),
            special_requirements: str = Field(default="", description="Special needs (high frequency, high current, miniaturization, etc.)")
        ) -> str:
            """Professional PCB layout guidance and design recommendations"""

            return f"""# 🔬 Professional PCB Layout Advisor

## 📋 Design Specifications
**Circuit**: {circuit_description}
**Board Size**: {board_size.title()} ({self._get_size_description(board_size)})
**Layer Count**: {layer_count} layers
**Special Requirements**: {special_requirements or "Standard design"}

## 🎯 PCB Layout Strategy

### 📐 Component Placement Optimization

**🔴 Power Section Layout**:
- Place voltage regulators near board edge for heat dissipation
- Use dedicated power planes (layer 2 for ground, layer 3 for power)
- Position bulk capacitors close to power input connectors
- Create power islands for different voltage domains (5V, 3.3V, analog)

**🧠 Microcontroller Placement**:
- Center microcontroller for equal trace lengths to peripherals
- Place crystal oscillator <1cm from MCU with guard traces
- Surround with decoupling capacitors (0.1µF + 10µF tantalum)
- Keep digital switching away from analog reference pins

**📡 High-Speed Signal Routing**:
- Route differential pairs with matched lengths (±0.1mm)
- Maintain 50Ω/100Ω impedance for single/differential signals
- Use via stitching every 5mm along transmission lines
- Avoid layer changes in critical timing paths

### ⚡ Advanced Layout Techniques

**🛡️ EMI/EMC Optimization**:
- Surround board perimeter with grounded guard traces
- Use ground pour with thermal reliefs for heat dissipation
- Route high-speed clocks away from board edges and connectors
- Add ferrite bead footprints on power and signal lines

**🌡️ Thermal Management**:
- Create thermal vias under high-power components (9 vias/cm²)
- Use copper pours for heat spreading (minimum 35µm thickness)
- Orient components for natural convection airflow
- Consider heat sinks and thermal interface materials

**🔧 Manufacturing Optimization**:
- Maintain minimum trace width: 0.1mm (4 mil) for standard fab
- Keep via sizes ≥0.2mm (8 mil) for reliable plating
- Use teardrop pads for mechanical strength
- Add fiducial markers for automated assembly

## 🎨 Layer Stack-Up Recommendations

{self._generate_layer_stackup(layer_count)}

## 📊 Design Rule Check (DRC) Guidelines

**✅ Critical Spacing Rules**:
- Trace to trace: ≥0.1mm (4 mil)
- Trace to via: ≥0.075mm (3 mil)
- Via to via: ≥0.2mm (8 mil)
- Copper to board edge: ≥0.2mm (8 mil)

**✅ Power Delivery Network**:
- Calculate voltage drop: <5% of supply voltage
- Size traces for 1A/mm² current density (external layers)
- Use multiple vias for high-current connections (>1A)
- Add test points for power rail verification

## 🚀 Professional PCB Features

**🔍 Testing & Debug**:
- Add test points on all critical signals (1mm diameter)
- Include JTAG/SWD connector for microcontroller debugging
- Route unused pins to test pads for future expansion
- Add LED indicators for power rails and critical signals

**🔧 Assembly & Rework**:
- Use standard component packages when possible
- Add component reference designators on silkscreen
- Include polarity markers for diodes, capacitors, connectors
- Leave space around components for rework access

**📋 Documentation Package**:
- Generate complete fabrication files (Gerber + Excellon)
- Create assembly drawings with component placement
- Provide bill of materials with manufacturer part numbers
- Include PCB stackup specification for fabrication

## 🎯 Ready for Professional PCB Design

**Say "Generate my PCB layout plan" and I'll create:**
1. **Detailed component placement strategy** optimized for your circuit
2. **Layer-by-layer routing plan** with impedance control
3. **Manufacturing file checklist** for fabrication
4. **Assembly documentation** for professional production
5. **Testing and validation procedures** for quality assurance

*Transform your breadboard prototype into a production-ready PCB design!*
"""

        def _get_size_description(self, size):
            """Get description for board size"""
            sizes = {
                "small": "compact designs, space-constrained applications",
                "medium": "standard development boards, general projects",
                "large": "complex systems, high component density"
            }
            return sizes.get(size, "custom sizing based on requirements")

        def _generate_layer_stackup(self, layer_count):
            """Generate appropriate layer stackup"""
            if layer_count == "2":
                return """
**2-Layer Stackup** (Cost-effective for simple designs):
- **Layer 1 (Top)**: Component placement + signal routing
- **Layer 2 (Bottom)**: Ground plane + power traces
- **Dielectric**: Standard FR4, 1.6mm thickness
- **Copper Weight**: 1oz (35µm) for standard current handling
"""
            elif layer_count == "4":
                return """
**4-Layer Stackup** (Recommended for mixed-signal designs):
- **Layer 1 (Top)**: Component placement + high-speed signals
- **Layer 2**: Ground plane (solid pour)
- **Layer 3**: Power planes (split for different voltages)
- **Layer 4 (Bottom)**: Low-speed signals + power distribution
- **Dielectric**: Controlled impedance FR4, 1.6mm total
- **Copper Weight**: 1oz standard, 2oz for power layers
"""
            else:
                return """
**6+ Layer Stackup** (High-performance designs):
- **Layer 1**: Components + critical signals
- **Layer 2**: Ground plane
- **Layer 3**: High-speed signal layer 1
- **Layer 4**: Power plane (+5V, +3.3V splits)
- **Layer 5**: High-speed signal layer 2
- **Layer 6+**: Additional signal/power layers as needed
- **Controlled Impedance**: 50Ω ±10% single-ended, 100Ω ±10% differential
"""