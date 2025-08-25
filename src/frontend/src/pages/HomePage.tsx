import React, { useEffect, useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import {
    Button,
    Spinner,
    Toast,
    ToastTitle,
    ToastBody,
    useToastController,
    Toaster
} from '@fluentui/react-components';
import {
    Add20Regular,
    ErrorCircle20Regular,
    Sparkle20Filled
} from '@fluentui/react-icons';
import '../styles/PlanPage.css';
import CoralShellColumn from '../coral/components/Layout/CoralShellColumn';
import CoralShellRow from '../coral/components/Layout/CoralShellRow';
import Content from '../coral/components/Content/Content';
import HomeInput from '@/components/content/HomeInput';
import { NewTaskService } from '../services/NewTaskService';
import PlanPanelLeft from '@/components/content/PlanPanelLeft';
import ContentToolbar from '@/coral/components/Content/ContentToolbar';
import { TaskService } from '../services/TaskService';
import { TeamConfig } from '../models/Team';
import { TeamService } from '../services/TeamService';
import InlineToaster, { useInlineToaster } from "../components/toast/InlineToaster";
/**
 * HomePage component - displays task lists and provides navigation
 * Accessible via the route "/"
 */
const HomePage: React.FC = () => {
    const navigate = useNavigate();
    const { dispatchToast } = useToastController("toast");
    const [selectedTeam, setSelectedTeam] = useState<TeamConfig | null>(null);
    const [isLoadingTeam, setIsLoadingTeam] = useState(true);
    const { showToast, dismissToast } = useInlineToaster();
    /**
     * Load teams and set default team on component mount
     */
    useEffect(() => {
        const loadDefaultTeam = async () => {
            let defaultTeam = TeamService.getStoredTeam();
            if (defaultTeam) {
                setSelectedTeam(defaultTeam);
                console.log('Default team loaded from storage:', defaultTeam.name);

                setIsLoadingTeam(false);
                return true;
            }
            setIsLoadingTeam(true);
            try {
                const teams = await TeamService.getUserTeams();
                console.log('All teams loaded:', teams);
                if (teams.length > 0) {
                    // Always prioritize "Business Operations Team" as default
                    const businessOpsTeam = teams.find(team => team.name === "Business Operations Team");
                    defaultTeam = businessOpsTeam || teams[0];
                    TeamService.storageTeam(defaultTeam);
                    setSelectedTeam(defaultTeam);
                    console.log('Default team loaded:', defaultTeam.name, 'with', defaultTeam.starting_tasks?.length || 0, 'starting tasks');
                    console.log('Team logo:', defaultTeam.logo);
                    console.log('Team description:', defaultTeam.description);
                    console.log('Is Business Operations Team:', defaultTeam.name === "Business Operations Team");
                } else {
                    console.log('No teams found - user needs to upload a team configuration');
                    // Even if no teams are found, we clear the loading state to show the "no team" message
                }
            } catch (error) {
                console.error('Error loading default team:', error);
            } finally {
                setIsLoadingTeam(false);
            }
        };

        loadDefaultTeam();
    }, []);

    /**
    * Handle new task creation from the "New task" button
    * Resets textarea to empty state on HomePage
    */
    const handleNewTaskButton = useCallback(() => {
        NewTaskService.handleNewTaskFromHome();
    }, []);

    /**
     * Handle team selection from the Settings button
     */
    const handleTeamSelect = useCallback((team: TeamConfig | null) => {
        setSelectedTeam(team);
        if (team) {
            showToast(`${team.name} team has been selected with ${team.agents.length} agents`, "success");
        } else {
            showToast(`No team is currently selected`, "info");
        }
    }, [showToast]);

    /**
     * Handle team upload completion - refresh team list and keep Business Operations Team as default
     */
    const handleTeamUpload = useCallback(async () => {
        try {
            const teams = await TeamService.getUserTeams();
            console.log('Teams refreshed after upload:', teams.length);

            if (teams.length > 0) {
                // Always keep "Business Operations Team" as default, even after new uploads
                const businessOpsTeam = teams.find(team => team.name === "Business Operations Team");
                const defaultTeam = businessOpsTeam || teams[0];
                setSelectedTeam(defaultTeam);
                console.log('Default team after upload:', defaultTeam.name);
                console.log('Business Operations Team remains default');
                showToast(`Team uploaded. ${defaultTeam.name} remains your default team.`, "success");

            }
        } catch (error) {
            console.error('Error refreshing teams after upload:', error);
        }
    }, [showToast]);


    return (
        <>
            <Toaster toasterId="toast" />
            <CoralShellColumn>
                <CoralShellRow>
                    <PlanPanelLeft
                        onNewTaskButton={handleNewTaskButton}
                        onTeamSelect={handleTeamSelect}
                        onTeamUpload={handleTeamUpload}
                        selectedTeam={selectedTeam}
                    />
                    <Content>
                        <ContentToolbar
                            panelTitle={"Multi-Agent Planner"}
                        ></ContentToolbar>
                        {!isLoadingTeam ? (
                            <HomeInput
                                selectedTeam={selectedTeam}
                            />
                        ) : (
                            // TODO MOVE THIS STYLE TO CSS 
                            <div style={{
                                display: 'flex',
                                justifyContent: 'center',
                                alignItems: 'center',
                                height: '200px'
                            }}>
                                <Spinner label="Loading team configuration..." />
                            </div>
                        )}
                    </Content>

                </CoralShellRow>
            </CoralShellColumn>
        </>
    );
};

export default HomePage;